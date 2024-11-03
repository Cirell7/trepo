from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request: HttpRequest) -> HttpResponse:
   return HttpResponse(content="9995")

def filic(request: HttpRequest) -> HttpResponse:
    return render(request, "first_site/filic.html")
