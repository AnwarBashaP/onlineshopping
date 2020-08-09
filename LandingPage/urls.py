from django.urls import path

from .views import LandPageView, signupView, loginView, User_LogoutAPIView

urlpatterns = [
    path('', LandPageView, name='home'),
    path('signup', signupView.as_view(), name='SignUp Page'),
    path('login', loginView, name='Login Page'),
    path('logout', User_LogoutAPIView, name='Logout'),
]