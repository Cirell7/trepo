from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def hello_world_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse(content="я @ ты @ я @ ты @я @ ты @ я @ ты @я @ ты @ я @ ты @")