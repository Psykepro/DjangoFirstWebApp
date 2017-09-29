import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Function based view
def home(request):
    num = random.randint(0, 10000000)
    return render(request, "base.html", {"html_var":"context variable", "num": num})