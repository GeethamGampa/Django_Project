from django.http import HttpResponse
from django.template import loader



def electronics(request):
    return HttpResponse("List of Electronics Products")

def apparel(request):
    return HttpResponse("List of Apparel Products")

def books(request):
    return HttpResponse("List of Books")

def store_home(request):
    template = loader.get_template('store_home.html')
    return HttpResponse(template.render())
