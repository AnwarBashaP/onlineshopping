from django.conf.urls.static import static
from django.urls import path

from Ecommerce import settings
from .views import Aboutview

urlpatterns = [
    path('', Aboutview.as_view(), name='About Page'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)