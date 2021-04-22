from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm


def register(request):
    """
    View that handles registering a user->profile
        TODO: handle form errors properly, change height and weight to integer fields and add labels
    """
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm, "pform": ProfileForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.first_name = profile_form.cleaned_data.get('first_name')
            user.last_name = profile_form.cleaned_data.get('last_name')
            user.profile.first_name = profile_form.cleaned_data.get('first_name')
            user.profile.last_name = profile_form.cleaned_data.get('last_name')
            user.profile.gender = profile_form.cleaned_data.get('gender')
            user.profile.birth_date = profile_form.cleaned_data.get('birth_date')
            user.profile.height = profile_form.cleaned_data.get('height')
            user.profile.weight = profile_form.cleaned_data.get('weight')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse("main_app:index"))
        return render(request, "registration/register.html", {'form': form, "pform": profile_form})


def index(request):
    return render(request, 'main_app/index.html')


def breathe(request):
    return render(request, 'main_app/breathe.html')


def plan_main(request):
    return render(request, 'main_app/plan_main.html')

def machines_view(request):
    return render(request, 'main_app/machines_view.html')


def plan(request):
    return render(request, 'main_app/plan.html')


def profile(request):
    return render(request, 'main_app/profile.html')


def machines(request):
    return render(request, 'main_app/machines_view.html')


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
            messages.error(request, ('Please correct the error below.'))
    else:
        # user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main_app/create_profile.html', {
        'profile_form': profile_form
    })

# def login(request, user):
#     return render(request, 'main_app/templates/registration/login.html')
