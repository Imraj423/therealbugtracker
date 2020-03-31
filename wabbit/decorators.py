from django.http import HttpResponse
from django.shortcuts import redirect


def unauth_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=['admin']):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = 'admin'
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(
                    'You are not authorized to access this content')
        return wrapper_func
    return decorator
