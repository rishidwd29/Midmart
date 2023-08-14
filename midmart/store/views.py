from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

def index(request):
    return render (request, "store/index.html")
def shop(request):
    Productform = productform()
    if request.method == 'POST':
        Productform = productform(request.POST, request.FILES)
        if Productform.is_valid():
                    Productform.save()
                    redirect('/shop')
    return render (request, "store/shop.html",{'productform': Productform})
def marketplace(request):
    allproducts = product.objects.all()
    return render (request, "store/marketplace.html",{"allproducts":allproducts})
# Create your views here.
