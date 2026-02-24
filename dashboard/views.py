from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib import messages
from core.models import Project, Skill, Message
from .forms import LoginForm, ProjectForm, SkillForm
from .decorators import login_required


# ── Authentication ──────────────────────────────────────────────

def login_view(request):
    if request.session.get('dashboard_user'):
        return redirect('dashboard:index')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None and user.is_staff:
                request.session['dashboard_user'] = user.username
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('dashboard:index')
            else:
                messages.error(request, 'Invalid credentials or insufficient permissions.')
    return render(request, 'dashboard/login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully.')
    return redirect('dashboard:login')


# ── Overview ─────────────────────────────────────────────────────

@login_required
def index(request):
    context = {
        'total_projects': Project.objects.count(),
        'total_skills': Skill.objects.count(),
        'total_messages': Message.objects.count(),
        'unread_messages': Message.objects.filter(is_read=False).count(),
        'recent_messages': Message.objects.filter(is_read=False)[:5],
        'recent_projects': Project.objects.all()[:5],
    }
    return render(request, 'dashboard/index.html', context)


# ── Projects CRUD ────────────────────────────────────────────────

@login_required
def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/projects.html', {'projects': projects})


@login_required
def project_create(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully.')
            return redirect('dashboard:projects')
    return render(request, 'dashboard/project_form.html', {'form': form, 'action': 'Create'})


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully.')
            return redirect('dashboard:projects')
    return render(request, 'dashboard/project_form.html', {'form': form, 'action': 'Edit', 'object': project})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted.')
        return redirect('dashboard:projects')
    return render(request, 'dashboard/confirm_delete.html', {'object': project, 'type': 'Project'})


# ── Skills CRUD ──────────────────────────────────────────────────

@login_required
def skills_list(request):
    skills = Skill.objects.all()
    return render(request, 'dashboard/skills.html', {'skills': skills})


@login_required
def skill_create(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill created successfully.')
            return redirect('dashboard:skills')
    return render(request, 'dashboard/skill_form.html', {'form': form, 'action': 'Create'})


@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated.')
            return redirect('dashboard:skills')
    return render(request, 'dashboard/skill_form.html', {'form': form, 'action': 'Edit', 'object': skill})


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted.')
        return redirect('dashboard:skills')
    return render(request, 'dashboard/confirm_delete.html', {'object': skill, 'type': 'Skill'})


# ── Messages ─────────────────────────────────────────────────────

@login_required
def messages_list(request):
    msgs = Message.objects.all()
    return render(request, 'dashboard/messages.html', {'msgs': msgs})


@login_required
def message_mark_read(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    msg.is_read = True
    msg.save()
    messages.success(request, 'Message marked as read.')
    return redirect('dashboard:messages')


@login_required
def message_delete(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        msg.delete()
        messages.success(request, 'Message deleted.')
        return redirect('dashboard:messages')
    return render(request, 'dashboard/confirm_delete.html', {'object': msg, 'type': 'Message'})
