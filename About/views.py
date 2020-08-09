from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from About.models import AboutModel


@permission_classes((AllowAny,))
# @permission_classes([IsAuthenticated])
class Aboutview(ListView):
    queryset =  AboutModel.objects.filter(is_active =  True).all().order_by('-CreatedDate')[:1]
    template_name = 'About/about.html'

    def get_context_data(self, *args,**kwargs):
        context = super(Aboutview,self).get_context_data(*args,**kwargs)

        return context