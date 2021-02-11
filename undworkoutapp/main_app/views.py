from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main_app/index.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

