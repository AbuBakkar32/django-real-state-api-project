from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    request.session['name'] = 'Sachin'
    print(request.session['name'])
    return HttpResponse("<h1 style='color:red;'><center><b>Hello, world. You're at the Blogs index.<b></center></h1>")
