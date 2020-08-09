
from django.urls import path
#
from .views import register_view, LoginApiview

urlpatterns = [
    path('register', register_view, name='Register'),
    path('loggedin', LoginApiview.as_view(), name='Logged In'),
]