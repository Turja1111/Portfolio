"""
Management command to seed the SUMS project into the portfolio database.
Run: python manage.py seed_sums
"""
from django.core.management.base import BaseCommand

from core.models import Project


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
        'attendance, course management, and administrative '
        'reporting.'
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


class Command(BaseCommand):
    help = 'Add the SUMS project to the portfolio if it does not already exist.'

    def handle(self, *args, **options):
        existing_projects = Project.objects.filter(
            github_url=SUMS_PROJECT['github_url'],
        ).order_by('id')

        if existing_projects.exists():
            project = existing_projects.first()
            created = False
            existing_projects.exclude(id=project.id).delete()
            for field, value in SUMS_PROJECT.items():
                setattr(project, field, value)
            project.save()
        else:
            project = Project.objects.create(**SUMS_PROJECT)
            created = True

        Project.objects.filter(
            title__icontains='Smart University Management System',
        ).exclude(id=project.id).delete()

        self.stdout.write(
            self.style.SUCCESS(
                f"{'Created' if created else 'Updated'} SUMS project in the database."
            )
        )
