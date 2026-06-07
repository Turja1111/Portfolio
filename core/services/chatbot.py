import json
import re
import urllib.error
import urllib.request

from django.conf import settings

from core.models import Project, Skill


class ChatbotError(Exception):
    pass


LOCAL_QA = [
    {
        "keywords": {"about", "who", "intro", "introduction", "tell"},
        "answer": (
            "Turja Das is a full stack developer focused on Python, Django, "
            "PostgreSQL, Docker, REST APIs, and polished web interfaces. "
            "He builds practical web systems with clean backend structure and "
            "user-friendly dashboards."
        ),
    },
    {
        "keywords": {"hire", "available", "work", "service", "freelance"},
        "answer": (
            "Turja is a good fit for Django web applications, REST API development, "
            "database-backed dashboards, deployment setup, portfolio systems, and "
            "full-stack feature development."
        ),
    },
    {
        "keywords": {"contact", "email", "reach", "linkedin", "connect"},
        "answer": (
            "You can contact Turja by email at saumik.das.turja@gmail.com or through "
            "LinkedIn: https://www.linkedin.com/in/saumik-das-turja."
        ),
    },
    {
        "keywords": {"cv", "resume", "download"},
        "answer": (
            "Turja's resume is available from the Resume button on the site. "
            "Direct download path: /cv/download/."
        ),
    },
    {
        "keywords": {"research", "paper", "publication", "doi", "zero-day", "intrusion"},
        "answer": (
            "Turja has published research titled 'A cross-dataset based zero-day "
            "intrusion detection system by integrating siamese network and "
            "reinforcement learning.' DOI: https://doi.org/10.1016/j.icte.2026.05.001."
        ),
    },
    {
        "keywords": {"backend", "api", "database", "postgresql", "django"},
        "answer": (
            "Turja's backend strengths include Django, Django REST Framework, "
            "PostgreSQL, REST API design, authentication flows, admin dashboards, "
            "and deployment-ready project structure."
        ),
    },
    {
        "keywords": {"frontend", "ui", "design", "tailwind", "interface"},
        "answer": (
            "On the frontend, Turja focuses on clean responsive interfaces, Tailwind CSS, "
            "dashboard layouts, interaction states, and polished portfolio/project pages."
        ),
    },
    {
        "keywords": {"deployment", "devops", "docker", "render", "pythonanywhere"},
        "answer": (
            "Turja has experience with deployment workflows using Docker, Render, "
            "PythonAnywhere, PostgreSQL configuration, static files, and production "
            "Django settings."
        ),
    },
]


def normalize_message(message):
    clean_message = " ".join(str(message).split())
    if not clean_message:
        raise ChatbotError("Please send a message first.")

    if len(clean_message) > settings.CHATBOT_MAX_MESSAGE_LENGTH:
        raise ChatbotError(
            f"Please keep messages under {settings.CHATBOT_MAX_MESSAGE_LENGTH} characters."
        )

    return clean_message


def tokenize(text):
    return set(re.findall(r"[a-z0-9+#.-]+", text.lower()))


def get_default_skills():
    return [
        "Python",
        "Django",
        "PostgreSQL",
        "Docker",
        "Linux",
        "CI/CD",
        "Django REST Framework",
        "JavaScript",
        "Tailwind CSS",
    ]


def format_projects():
    projects = list(Project.objects.all()[:8])
    if not projects:
        return (
            "The portfolio is ready to show projects once they are added in the dashboard. "
            "A key featured project is SUMS, the Smart University Management System."
        )

    lines = []
    for project in projects:
        links = []
        if project.live_url:
            links.append(f"Live: {project.live_url}")
        if project.github_url:
            links.append(f"GitHub: {project.github_url}")
        suffix = f" {' | '.join(links)}" if links else ""
        lines.append(f"{project.title}: {project.description}{suffix}")

    return "Featured project information:\n" + "\n".join(f"- {line}" for line in lines)


def format_skills():
    skills = list(Skill.objects.all()[:30])
    if not skills:
        return "Turja's core skills include " + ", ".join(get_default_skills()) + "."

    skill_text = ", ".join(
        f"{skill.name} ({skill.get_category_display()}, {skill.proficiency}%)"
        for skill in skills
    )
    return f"Turja's listed skills are: {skill_text}."


def answer_about_sums():
    project = (
        Project.objects.filter(title__icontains="SUMS").first()
        or Project.objects.filter(title__icontains="Smart University").first()
    )

    if project:
        links = []
        if project.live_url:
            links.append(f"Live: {project.live_url}")
        if project.github_url:
            links.append(f"GitHub: {project.github_url}")
        link_text = f" {' | '.join(links)}" if links else ""
        return f"{project.title}: {project.description}{link_text}"

    return (
        "SUMS is a Smart University Management System with role-based dashboards "
        "for students, teachers, and admins, 40+ REST API endpoints, AI-driven "
        "insights, and a modern interface."
    )


def answer_local_question(message):
    words = tokenize(message)

    if {"sums", "university", "management", "student", "teacher", "admin"} & words:
        return answer_about_sums()

    if {"project", "projects", "portfolio", "github", "live"} & words:
        return format_projects()

    if {"skill", "skills", "stack", "technology", "technologies", "tech"} & words:
        return format_skills()

    direct_topics = [
        ({"research", "paper", "publication", "doi", "zero-day", "intrusion"}, LOCAL_QA[4]["answer"]),
        ({"contact", "email", "reach", "linkedin", "connect"}, LOCAL_QA[2]["answer"]),
        ({"cv", "resume", "download"}, LOCAL_QA[3]["answer"]),
        ({"hire", "available", "work", "service", "freelance"}, LOCAL_QA[1]["answer"]),
        ({"deployment", "devops", "docker", "render", "pythonanywhere"}, LOCAL_QA[7]["answer"]),
        ({"backend", "api", "database", "postgresql", "django"}, LOCAL_QA[5]["answer"]),
        ({"frontend", "ui", "design", "tailwind", "interface"}, LOCAL_QA[6]["answer"]),
    ]
    for keywords, answer in direct_topics:
        if words & keywords:
            return answer

    best_answer = None
    best_score = 0
    for item in LOCAL_QA:
        score = len(words & item["keywords"])
        if score > best_score:
            best_score = score
            best_answer = item["answer"]

    if best_answer:
        return best_answer

    return (
        "I can help with Turja's projects, skills, research, resume, contact details, "
        "backend experience, frontend work, and deployment background. Try asking: "
        "'Tell me about SUMS', 'What skills does Turja use?', or 'How can I contact Turja?'"
    )


def build_portfolio_context():
    projects = Project.objects.all()[:8]
    skills = Skill.objects.all()[:30]

    project_lines = []
    for project in projects:
        links = []
        if project.github_url:
            links.append(f"GitHub: {project.github_url}")
        if project.live_url:
            links.append(f"Live: {project.live_url}")
        link_text = f" ({'; '.join(links)})" if links else ""
        project_lines.append(
            f"- {project.title}: {project.description} "
            f"Tech: {project.tech_stack or 'Not listed'}.{link_text}"
        )

    skill_lines = [
        f"- {skill.name} ({skill.get_category_display()}, {skill.proficiency}%)"
        for skill in skills
    ]

    return "\n".join([
        "Portfolio owner: Turja Das.",
        "Role: Full Stack Developer.",
        "Core focus: Python, Django, PostgreSQL, Docker, DevOps, REST APIs, and polished web interfaces.",
        "Contact email: saumik.das.turja@gmail.com.",
        "LinkedIn: https://www.linkedin.com/in/saumik-das-turja.",
        "GitHub: https://github.com/Turja1111.",
        "CV download path: /cv/download/.",
        "Research: A cross-dataset based zero-day intrusion detection system by integrating siamese network and reinforcement learning. DOI: https://doi.org/10.1016/j.icte.2026.05.001.",
        "Projects:",
        "\n".join(project_lines) if project_lines else "- No projects are currently listed.",
        "Skills:",
        "\n".join(skill_lines) if skill_lines else "- Python, Django, PostgreSQL, Docker, Linux, CI/CD.",
    ])


def ask_openrouter(clean_message):
    payload = {
        "model": settings.OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are the portfolio assistant for Turja Das. "
                    "Answer questions about Turja's projects, skills, research, CV, and contact details. "
                    "Use the provided portfolio context as your source of truth. "
                    "Be concise, friendly, and professional. "
                    "If a question is unrelated to Turja's portfolio, politely guide the visitor back to projects, skills, research, or contact. "
                    "Never claim Turja has skills, jobs, degrees, or achievements that are not in the context.\n\n"
                    f"Portfolio context:\n{build_portfolio_context()}"
                ),
            },
            {"role": "user", "content": clean_message},
        ],
        "temperature": 0.4,
        "max_tokens": 420,
        "stream": False,
        "reasoning": {"enabled": True},
    }

    request = urllib.request.Request(
        settings.OPENROUTER_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))

    return data["choices"][0]["message"]["content"].strip()


def ask_deepseek(clean_message):
    payload = {
        "model": settings.DEEPSEEK_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are the portfolio assistant for Turja Das. "
                    "Answer questions about Turja's projects, skills, research, CV, and contact details. "
                    "Use the provided portfolio context as your source of truth. "
                    "Be concise, friendly, and professional. "
                    "If a question is unrelated to Turja's portfolio, politely guide the visitor back to projects, skills, research, or contact. "
                    "Never claim Turja has skills, jobs, degrees, or achievements that are not in the context.\n\n"
                    f"Portfolio context:\n{build_portfolio_context()}"
                ),
            },
            {"role": "user", "content": clean_message},
        ],
        "temperature": 0.4,
        "max_tokens": 420,
        "stream": False,
    }

    request = urllib.request.Request(
        settings.DEEPSEEK_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))

    return data["choices"][0]["message"]["content"].strip()


def ask_portfolio_assistant(message):
    clean_message = normalize_message(message)

    if settings.CHATBOT_USE_OPENROUTER and settings.OPENROUTER_API_KEY:
        try:
            return ask_openrouter(clean_message)
        except (
            urllib.error.HTTPError,
            urllib.error.URLError,
            TimeoutError,
            json.JSONDecodeError,
            KeyError,
            IndexError,
            TypeError,
        ):
            return answer_local_question(clean_message)

    if settings.CHATBOT_USE_DEEPSEEK and settings.DEEPSEEK_API_KEY:
        try:
            return ask_deepseek(clean_message)
        except (
            urllib.error.HTTPError,
            urllib.error.URLError,
            TimeoutError,
            json.JSONDecodeError,
            KeyError,
            IndexError,
            TypeError,
        ):
            return answer_local_question(clean_message)

    return answer_local_question(clean_message)
