from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = { "header" : "Hello Django", "message" : "Welcome to Python!"}
    return render(request, "realty/index.html", context=data)