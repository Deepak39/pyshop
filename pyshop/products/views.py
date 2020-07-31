from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(req):
    products = Product.objects.all()
    return render(req, "index.html", {"products": products})

def new_products(req):
    return HttpResponse("New Products are Here!")