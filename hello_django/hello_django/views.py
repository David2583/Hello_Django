from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, "about.html", {"greeting": "Hello"})
def home(request):
    return render(request, "home.html")