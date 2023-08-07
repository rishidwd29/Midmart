from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render (request, "store/index.html")
def shop(request):
    return render (request, "store/shop.html")
def marketplace(request):
    return render (request, "store/marketplace.html")
# Create your views here.
