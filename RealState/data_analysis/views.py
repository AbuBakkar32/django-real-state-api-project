from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def data_analysis(request):
    return HttpResponse(
        "<h1 style='color:black;'><center><b>Hello, world. You're at the data analysis index.<b></center></h1>")
