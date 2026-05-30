"""
Management command to seed the SUMS project into the portfolio database.
Run: python manage.py seed_sums
"""
from django.core.management.base import BaseCommand

from core.models import Project


class Command(BaseCommand):
    help = 'Add the SUMS project to the portfolio if it does not already exist.'

    def handle(self, *args, **options):
        project, created = Project.objects.update_or_create(
            title='SUMS - Smart University Management System',
            defaults={
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
            },
        )

        if created:
            self.stdout.write(self.style.SUCCESS(
                'Created SUMS project in the database.'
            ))
        else:
            self.stdout.write(self.style.SUCCESS(
                'Updated existing SUMS project in the database.'
            ))
