from .models import Profile, User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'first_name', 'last_name', 'gender', 'birth_date')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender', 'birth_date', 'height', 'weight')
