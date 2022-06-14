from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


def home(request):
    return render(request, 'home.html')


def products(request):
    return render(request, 'products.html')


def contact(request):
    return render(request, 'contact.html')
    

def index(request):
    # return HttpResponse('Welcome to my home page')
    return render(request, 'index.html')


def about(request):
    return HttpResponse('This is about page')


def search(request, keyword, page):
    return HttpResponse(f'Search for {keyword} page : {page}')


def maps(request):
    type = request.GET.get('type','hybrid')   
    lat = request.GET.get('lat','13.039303')   
    lon = request.GET.get('lon','100.089488')   
    zoom = request.GET.get('z',10) 

    return HttpResponse(f"<h4>Map type: {type}</h4><br>Location: {lat},{lon}<br>Zoom: {zoom}")  


def test(request):
    dt = date.today()
    data = {
        'site': {'title': 'Django Framework', 'message': 'Hello Python Django'}, # dictionary
        'colors': ['red', 'greed', 'blue'], # list
        'date': dt # object
    }
    return render(request, 'test.html', data)