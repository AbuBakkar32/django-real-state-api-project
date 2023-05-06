from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def machine_learning(request):
    return HttpResponse(
        "<h1 style='color:red;'><center><b>Hello, world. You're at the machine learning index.<b></center></h1>")
