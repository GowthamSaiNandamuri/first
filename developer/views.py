from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('this is my first fbv')
# Create your views here.
