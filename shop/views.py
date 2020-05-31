from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    cetagory = Product.objects.all()

    params = {'allProds':allProds,'cta':cetagory }
    return render(request, 'shop/index.html', params)

def about(request):
    products = Product.objects.all()
    item = {'product':products }
    return render(request, 'shop/about.html',item)

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return HttpResponse("We are at search")

def productview(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")

