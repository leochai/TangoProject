from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!<br/> <a href='/rango/about'>About</a>")
# Create your views here.

def about(request):
    return HttpResponse("Rango says here is the about page <br/><a href='/rango/'>Index</a>")