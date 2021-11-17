from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kohli(request):
    return HttpResponse('Kohli the aggressive man')

def rohit(request):
    return HttpResponse('Rohit the HIt ManN')