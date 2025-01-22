from django.shortcuts import render
from django.http import HttpResponse

def product(request):
    return HttpResponse('Product Loaded!')
# Create your tests here.
