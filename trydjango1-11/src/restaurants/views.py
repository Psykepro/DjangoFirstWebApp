from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Function based view
def home(request):
    html_var = 'html'
    html = f"""<!DOCTYPE html><html lang="en"><head></head><body><h1> HALLA </h1><p>This is {html_var} coming through</p></body></html>"""
    return HttpResponse(html) 
    # return render(request, "home.html", {}