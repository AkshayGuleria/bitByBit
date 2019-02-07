from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<h1>Gnillib Home</h1>')

def contact(request):
    return HttpResponse('<h1>Gnillib Contact</h1> \n '
                        '<h2>Akshay Guleria</h2>')