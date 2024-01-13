from functools import wraps
from django.shortcuts import redirect, render

def check_role(view_func):
    @wraps(view_func)
    def _wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('/admin/')
            elif request.user.is_staff and request.user.username == 'trainStationAdmin':
                return redirect('/trainstation/admin/')
            elif request.user.is_staff and request.user.username == 'bookingAdmin':
                return redirect('/booking/admin/')

        return view_func(request,*args,**kwargs)
    return _wrapped_view

