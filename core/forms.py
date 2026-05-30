from django import forms
from .models import Message


CONTACT_INPUT_CLASS = (
    'w-full rounded-xl border border-white/10 bg-slate-950/50 px-4 py-3 '
    'text-white placeholder-slate-500 outline-none transition '
    'focus:border-cyan-300/70 focus:ring-2 focus:ring-cyan-300/15'
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'subject', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': CONTACT_INPUT_CLASS,
                'placeholder': 'Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': CONTACT_INPUT_CLASS,
                'placeholder': 'your@email.com',
            }),
            'phone': forms.TextInput(attrs={
                'class': CONTACT_INPUT_CLASS,
                'placeholder': 'Phone (optional)',
            }),
            'subject': forms.TextInput(attrs={
                'class': CONTACT_INPUT_CLASS,
                'placeholder': 'Subject',
            }),
            'body': forms.Textarea(attrs={
                'class': CONTACT_INPUT_CLASS,
                'placeholder': 'Your message...',
                'rows': 5,
            }),
        }
