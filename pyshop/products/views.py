from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return HttpResponse("Hello to Products Apps.")

def new_products(req):
    return HttpResponse("New Products are Here!")