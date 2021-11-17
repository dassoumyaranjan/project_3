from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    return HttpResponse('<h1>All the best Everyone</h1>')

def dhoni(request):
    return HttpResponse('<marquee>Dhoni and Raina are best Brothers</marquee>')
