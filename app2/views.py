import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2(request):
    return HttpResponse('This is my second Application')
