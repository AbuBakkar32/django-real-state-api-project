from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def deep_learning(request):
    return HttpResponse(
        "<h1 style='color:black;'><center><b>Hello, world. You're at the deep learning index.<b></center></h1>")
