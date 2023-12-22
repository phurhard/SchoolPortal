from functools import wraps
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

def teacher_only(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # get the user role
        try:
            if request.user.teacher:
                return func(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return redirect('/student/')
    return wrapper
