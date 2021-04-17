from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#
from .views import register_view, LoginApiview, ContactUsView

urlpatterns = [
    path('register', register_view, name='Register'),
    path('loggedin', LoginApiview.as_view(), name='Logged In'),
    path('contact', ContactUsView, name='contact'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)