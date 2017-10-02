import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# Function based view

class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {
        }
        print(kwargs)
        return render(request, "contact.html", context)

def contact(request):
    context = {
    }
    return render(request, "contact.html", context)

def about(request):
    context = {
    }
    return render(request, "about.html", context)

def home(request):
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
    return render(request, "home.html", context)


