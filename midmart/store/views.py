from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

def index(request):
    return render (request, "store/index.html")
def shop(request):
    try:
        Productform = productform()
        if request.method == 'POST':
            Productform = productform(request.POST, request.FILES)
            if installmentForm.is_valid():
                        ProductForm.save()
                        redirect('/shop')
    except:
        return HttpResponse("fault in backend")
    return render (request, "store/shop.html",{'productform': Productform})
def marketplace(request):
    return render (request, "store/marketplace.html")
# Create your views here.
