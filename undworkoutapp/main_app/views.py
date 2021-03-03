from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("main_app:index"))
        return render(request, "registration/register.html", {'form': form})


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


def create_profile(request):
    if request.method == 'POST':
        # user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        # if user_form.is_valid() and profile_form.is_valid():
        if profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('main_app:index')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        # user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main_app/create_profile.html', {
        'profile_form': profile_form
    })

# def login(request, user):
#     return render(request, 'main_app/templates/registration/login.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
