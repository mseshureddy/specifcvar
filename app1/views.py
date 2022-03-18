from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def app1(request):
    return HttpResponse('<marquee><h>This is my first Application</h1></marquee>')
