from django.http import HttpResponseRedirect
from functools import wraps

from rest_framework.exceptions import ValidationError


def Loginverifications(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        # for i in request.session.values():
        if "token" in request.session:
            if "user" in request.session:
                print("data")
                return HttpResponseRedirect("/home")
        return function(request, *args, **kwargs)
    return wrap