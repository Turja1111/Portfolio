<div align="center">

# ✦ Turja Das — Portfolio

**A premium, production-grade portfolio built with Django, PostgreSQL & Docker**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.0-092E20?logo=django&logoColor=white)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://docker.com)
[![CI](https://img.shields.io/github/actions/workflow/status/Turja1111/Portfolio/deploy.yml?label=CI&logo=github)](https://github.com/Turja1111/Portfolio/actions)
[![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render&logoColor=white)](https://render.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<br />

> A single-page developer portfolio with an animated dark-space aesthetic, glassmorphism UI, scroll-triggered animations, and a full admin dashboard — all backed by Django & PostgreSQL.

<br />

[**Live Demo →**](#) · [**View Research Paper →**](#research) · [**Download CV →**](#)

</div>

---

## 🎯 Why This Project?

This isn't a static HTML page — it's a **full-stack web application** that demonstrates production-level engineering:

- **Backend-driven content**: Projects, skills, and messages are stored in PostgreSQL and managed through a secure admin dashboard.
- **CI/CD pipeline**: Every push runs flake8 lint + Django system checks via GitHub Actions.
- **One-click deploy**: Render blueprint (`render.yaml`) deploys the entire stack in minutes.
- **Professional UI/UX**: Particle backgrounds, cursor-tracking glow, scroll progress, typewriter effects, and micro-animations — all built with zero JavaScript frameworks.

---

## ✨ Features

| Category | Details |
|----------|---------|
| ✨ **Glassmorphism UI** | Frosted-glass cards, gradient borders, and a dark-space color system |
| 🎨 **Particle Background** | Live canvas-rendered particles with proximity-based connections |
| ✍️ **Typewriter Effect** | Rotating tagline with smooth type/delete animation |
| 🖱️ **Cursor Glow** | Radial gradient that follows mouse movement |
| 📊 **Animated Skill Bars** | Scroll-triggered progress bars with gradient fills |
| 🔢 **Counter Animations** | Numbers that count up on scroll with easing |
| 📱 **Fully Responsive** | Mobile-first layout with collapsible navigation |
| 🛠️ **Admin Dashboard** | Session-based auth, CRUD for projects/skills, message inbox |
| 💬 **Contact Form** | Messages saved directly to PostgreSQL |
| 📄 **CV Download** | Floating action button + navbar link for resume download |
| 📑 **Research Showcase** | Published paper display with in-browser PDF viewer |
| 📜 **Scroll Progress** | Animated gradient progress bar at top of viewport |
| ♿ **Reduced Motion** | Respects `prefers-reduced-motion` for accessibility |
| 🔍 **SEO Optimized** | Open Graph tags, semantic HTML, proper heading hierarchy |

---

## 📂 Project Structure

```
Portfolio/
├── core/                       # Main portfolio app
│   ├── models.py               # Project, Skill, Contact models
│   ├── views.py                # Home, CV download, research paper views
│   ├── forms.py                # Contact form with validation
│   ├── urls.py                 # URL routing
│   └── templates/core/
│       ├── base.html           # Master layout (particles, nav, footer, JS)
│       └── home.html           # Single-page portfolio sections
├── dashboard/                  # Admin dashboard app
│   ├── views.py                # CRUD views for projects, skills, messages
│   ├── forms.py                # Dashboard forms
│   └── templates/dashboard/    # Dashboard templates
├── portfolio/                  # Django project config
│   └── settings/
│       ├── base.py             # Shared settings
│       ├── development.py      # Local dev (SQLite)
│       └── production.py       # Production (PostgreSQL, WhiteNoise)
├── static/picture/             # Profile image
├── cv/                         # Downloadable CV PDF
├── research/                   # Published research paper PDF
├── docker-compose.yml          # Local Docker environment
├── Dockerfile                  # Container build
├── render.yaml                 # Render deploy blueprint
├── build.sh                    # Production build script
├── requirements.txt            # Python dependencies
└── .github/workflows/
    └── deploy.yml              # CI pipeline (lint + check)
```

---

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/Turja1111/Portfolio.git
cd Portfolio

# Copy environment variables
cp .env.example .env
# Edit .env with your values

# Build and start
docker-compose up --build -d

# Apply migrations
docker-compose exec web python manage.py migrate

# Create admin user
docker-compose exec web python manage.py createsuperuser

# Visit http://localhost:8000
```

### Option 2: Manual Setup

```bash
# Clone
git clone https://github.com/Turja1111/Portfolio.git
cd Portfolio

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Environment variables
cp .env.example .env
# Edit .env — set SECRET_KEY, DATABASE_URL, etc.

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Start development server
python manage.py runserver
```

---

## ⚙️ Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | *(required)* |
| `DEBUG` | Enable debug mode | `False` |
| `DATABASE_URL` | PostgreSQL connection string | `sqlite:///db.sqlite3` |
| `DJANGO_SETTINGS_MODULE` | Settings module path | `portfolio.settings.development` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |

---

## 🌐 Deploy to Render

This project includes a **`render.yaml` blueprint** for one-click deployment:

1. Fork this repository
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Click **New → Blueprint Instance**
4. Connect your forked repo
5. Render auto-detects `render.yaml` and provisions:
   - Python web service (free tier)
   - PostgreSQL database (free tier)
   - Auto-generated `SECRET_KEY`

> **Note:** The free-tier web service spins down after inactivity. First request after idle may take ~30 seconds.

---

## 🧪 CI Pipeline

Every push to `main` triggers:

```
✓ flake8 lint (max line length: 120)
✓ Django system check
```

See [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) for the full workflow.

---

## 📖 Published Research

> **"A cross-dataset based zero-day intrusion detection system by integrating siamese network and reinforcement learning"**
>
> *Published in ICT Express, 2026*
>
> DOI: [10.1016/j.icte.2026.05.001](https://doi.org/10.1016/j.icte.2026.05.001)

This paper presents a novel approach to zero-day intrusion detection, combining **Siamese networks** with **reinforcement learning** for robust cross-dataset generalization in cybersecurity.

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.11 |
| **Framework** | Django 5.0 |
| **Database** | PostgreSQL 16 |
| **Styling** | Tailwind CSS (CDN) + Custom CSS |
| **Static Files** | WhiteNoise |
| **WSGI Server** | Gunicorn |
| **Containerization** | Docker + Docker Compose |
| **CI/CD** | GitHub Actions |
| **Hosting** | Render (free tier) |
| **Icons** | Font Awesome 6.5 |
| **Fonts** | Inter, JetBrains Mono (Google Fonts) |

</div>

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m "Add amazing feature"`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ by [Turja Das](https://github.com/Turja1111)**

*Full-Stack Developer · Django · PostgreSQL · Docker · DevOps*

[![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white)](https://github.com/Turja1111)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/saumik-das-turja)

</div>
