from django.db import migrations


SUMS_PROJECT = {
    'title': 'SUMS - Smart University Management System',
    'description': (
        'A full-stack university management platform with role-based '
        'dashboards for Students, Teachers, and Admins, powered by '
        'AI-driven insights, 40+ REST API endpoints, and real-time analytics.'
    ),
    'long_description': (
        'SUMS is a comprehensive Smart University Management System '
        'designed to streamline academic operations. It features '
        'three dedicated dashboards (Student, Teacher, Admin), '
        '40+ API endpoints, 3 AI-powered features for intelligent '
        'analytics, and a modern glassmorphism UI. Built with '
        'Django REST Framework on the backend and a responsive '
        'frontend, the system handles enrollment, grading, '
        'attendance, course management, and administrative reporting.'
    ),
    'tech_stack': (
        'Python, Django, Django REST Framework, PostgreSQL, '
        'JavaScript, Tailwind CSS, AI/ML, PythonAnywhere'
    ),
    'github_url': (
        'https://github.com/Turja1111/'
        'Smart-University-Management-System'
    ),
    'live_url': 'https://turja221b.pythonanywhere.com/login/',
    'image_url': '',
    'featured': True,
    'order': 1,
}


def seed_sums_project(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    existing_projects = Project.objects.filter(
        github_url=SUMS_PROJECT['github_url'],
    ).order_by('id')

    if existing_projects.exists():
        project = existing_projects.first()
        existing_projects.exclude(id=project.id).delete()
        for field, value in SUMS_PROJECT.items():
            setattr(project, field, value)
        project.save()
    else:
        project = Project.objects.create(**SUMS_PROJECT)

    Project.objects.filter(
        title__icontains='Smart University Management System',
    ).exclude(id=project.id).delete()


def unseed_sums_project(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(github_url=SUMS_PROJECT['github_url']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_skill_icon'),
    ]

    operations = [
        migrations.RunPython(seed_sums_project, unseed_sums_project),
    ]
