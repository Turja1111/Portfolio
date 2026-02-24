from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def login_required(view_func):
    """Custom login required decorator using session auth."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('dashboard_user'):
            messages.warning(request, 'Please log in to access the dashboard.')
            return redirect('dashboard:login')
        return view_func(request, *args, **kwargs)
    return wrapper
