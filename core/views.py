from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill
from .forms import ContactForm


RESEARCH_PAPER_FILENAME = 'A cross-dataset based zero-day intrusion detection system by integrating.pdf'


def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    form = ContactForm()
    default_skills = [
        {'name': 'Python', 'icon': 'fa-brands fa-python', 'pct': 92},
        {'name': 'Django', 'icon': 'fa-solid fa-code', 'pct': 90},
        {'name': 'PostgreSQL', 'icon': 'fa-solid fa-database', 'pct': 86},
        {'name': 'Docker', 'icon': 'fa-brands fa-docker', 'pct': 82},
        {'name': 'Linux', 'icon': 'fa-brands fa-linux', 'pct': 78},
        {'name': 'CI/CD', 'icon': 'fa-solid fa-code-branch', 'pct': 76},
    ]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent! I'll get back to you soon.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")

    # Group skills by category
    skill_categories = {}
    for skill in skills:
        cat = skill.get_category_display()
        if cat not in skill_categories:
            skill_categories[cat] = []
        skill_categories[cat].append(skill)

    context = {
        'projects': projects,
        'skills': skills,
        'skill_categories': skill_categories,
        'default_skills': default_skills,
        'form': form,
    }
    return render(request, 'core/home.html', context)


def research_paper_pdf(request):
    paper_path = settings.BASE_DIR / 'research' / RESEARCH_PAPER_FILENAME
    if not paper_path.exists():
        raise Http404('Research paper PDF not found.')

    return FileResponse(
        paper_path.open('rb'),
        content_type='application/pdf',
        filename=RESEARCH_PAPER_FILENAME,
    )
