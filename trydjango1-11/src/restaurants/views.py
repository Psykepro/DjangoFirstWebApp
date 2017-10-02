import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
# Function based view
from .models import RestaurantLocation

def restaurant_list_view(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)
