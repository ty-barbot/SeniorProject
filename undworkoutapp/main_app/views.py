import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from .models import Profile, Machines
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
    return render(request, 'main_app/plan.html', {"machine_list": Machines.objects.all()})


def profile(request):
    if request.method == 'POST':
        user = request.POST.get("user_profile")
        new_height = request.POST.get("new_height")
        new_weight = request.POST.get("new_weight")
        new_birthdate = request.POST.get("new_birthdate")
        user_id = User.objects.get(username=user)
        user_profile = Profile.objects.get(user=user_id)
        if new_weight:
            user_profile.weight = new_weight
        if new_height:
            user_profile.height = new_height
        if new_birthdate:
            try:
                print(new_birthdate)
                datetime.datetime.strptime(new_birthdate, "%Y-%m-%d")
                user_profile.birth_date = new_birthdate
            except ValueError as e:
                print("erorr1")
                messages.error(request, 'llo world.')
                # return redirect('main_app:profile')
                return render(request, 'main_app/profile.html')
        user_profile.save()
        messages.add_message(request, messages.WARNING, "")
        # return redirect('/profile/')
        return render(request, 'main_app/profile.html')
    else:
        return render(request, 'main_app/profile.html')


class EditProfile(TemplateView):
    template_name = "main_app/profile.html"

    def post(self, request):
        user = request.POST.get("user_profile")
        new_height = request.POST.get("new_height")
        new_weight = request.POST.get("new_weight")
        new_birthdate = request.POST.get("new_birthdate")
        user_id = User.objects.get(username=user)
        user_profile = Profile.objects.get(user=user_id)
        if new_weight:
            user_profile.weight = new_weight
        if new_height:
            user_profile.height = new_height
        if new_birthdate:
            try:
                datetime.datetime.strptime(new_birthdate, "%Y-%m-%d")
            except ValueError as e:
                print("error")
                messages.error(request, 'Document deleted.')
                messages.add_message(self.request, messages.WARNING, "")
                # return redirect('main_app:profile')
                # return render(request, 'main_app/profile.html')
        user_profile.save()
        messages.success(request, 'Profile saved successfully.')
        messages.add_message(self.request, messages.WARNING, "")
        return redirect('main_app:profile')
        # return render(request, 'main_app/profile.html')


@require_http_methods(["POST"])
def edit_profile(request):
    user = request.POST.get("user_profile")
    new_height = request.POST.get("new_height")
    new_weight = request.POST.get("new_weight")
    new_birthdate = request.POST.get("new_birthdate")
    user_id = User.objects.get(username=user)
    user_profile = Profile.objects.get(user=user_id)
    if new_weight:
        user_profile.weight = new_weight
    if new_height:
        user_profile.height = new_height
    if new_birthdate:
        try:
            datetime.datetime.strptime(new_birthdate, "%Y-%m-%d")
            user_profile.birth_date = new_birthdate
        except ValueError as e:
            print("erorr1")
            messages.error(request, 'llo world.')
            return redirect('main_app:profile')
            # return render(request, 'main_app/profile.html')
    user_profile.save()
    messages.add_message(request, messages.WARNING, "")
    return redirect('main_app:profile')
    # return render(request, 'main_app/profile.html')


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

def machines_view(request):
    return render(request, 'main_app/machines_view.html', {"machine_list": Machines.objects.all()})
def machines_view_Arm(request):
    return render(request, 'main_app/machines_view.html', {"machine_list": Machines.objects.filter(type="Arm")})
def machines_view_Leg(request):
    return render(request, 'main_app/machines_view.html', {"machine_list": Machines.objects.filter(type="Leg")})
def machines_view_Cardio(request):
    return render(request, 'main_app/machines_view.html', {"machine_list": Machines.objects.filter(type="Cardio")})
def machines_view_Abs(request):
    return render(request, 'main_app/machines_view.html', {"machine_list": Machines.objects.filter(type="Abs")})

# def login(request, user):
#     return render(request, 'main_app/templates/registration/login.html')
