import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
# Function based view

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            random.randint(0, 10000000),
            random.randint(0, 10000000),
            random.randint(0, 10000000)
        ]
        conditional_bool_item = True
        if conditional_bool_item:
            num = random.randint(0, 10000000)
        context = {
                "num": num,
                "some_list":some_list
        }
        print(context)
        return context


