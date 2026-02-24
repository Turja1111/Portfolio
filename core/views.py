from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill
from .forms import ContactForm


def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    form = ContactForm()

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
        'form': form,
    }
    return render(request, 'core/home.html', context)
