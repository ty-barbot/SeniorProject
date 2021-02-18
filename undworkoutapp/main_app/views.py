from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'main_app/index.html')


def breathe(request):
    return render(request, 'main_app/breathe.html')


def plan(request):
    return render(request, 'main_app/plan.html')


def profile(request):
    return render(request, 'main_app/profile.html')


def machines(request):
    return render(request, 'main_app/machines.html')


def workout(request):
    return render(request, 'main_app/workout.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
