from django.shortcuts import render
from .models import Product,Contact
from math import ceil
from django.http import HttpResponse

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    # print(catprods)
    cats = {item['category'] for item in catprods}
    print(cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    cetagory = Product.objects.all()

    params = {'allProds':allProds,'cta':cetagory }
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    name = request.POST.get('name','')
    phone = request.POST.get('phone','')
    email = request.POST.get('email','')
    qury = request.POST.get('qury','')
    con = Contact(name=name,phone=phone,email =email,qury=qury)
    con.save()

    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productview(request,myid):
    product = Product.objects.filter(id=myid)
    look = {'product' : product[0]}
    return render(request,'shop/pro.html',look)

def checkout(request):
    return render(request, 'shop/checkout.html')

