from django import forms
from core.models import Project, Skill


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg bg-slate-700 border border-slate-600 text-white placeholder-slate-400 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition',
            'placeholder': 'Username',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg bg-slate-700 border border-slate-600 text-white placeholder-slate-400 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition',
            'placeholder': 'Password',
        })
    )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'long_description', 'tech_stack',
                  'github_url', 'live_url', 'image_url', 'featured', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'dash-input'}),
            'description': forms.Textarea(attrs={'class': 'dash-input', 'rows': 3}),
            'long_description': forms.Textarea(attrs={'class': 'dash-input', 'rows': 4}),
            'tech_stack': forms.TextInput(attrs={'class': 'dash-input', 'placeholder': 'Python, Django, Docker'}),
            'github_url': forms.URLInput(attrs={'class': 'dash-input'}),
            'live_url': forms.URLInput(attrs={'class': 'dash-input'}),
            'image_url': forms.URLInput(attrs={'class': 'dash-input'}),
            'order': forms.NumberInput(attrs={'class': 'dash-input'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'category', 'icon', 'proficiency', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'dash-input'}),
            'category': forms.Select(attrs={'class': 'dash-input'}),
            'icon': forms.TextInput(attrs={'class': 'dash-input', 'placeholder': '🐍 or fa-python'}),
            'proficiency': forms.NumberInput(attrs={'class': 'dash-input', 'min': 0, 'max': 100}),
            'order': forms.NumberInput(attrs={'class': 'dash-input'}),
        }
