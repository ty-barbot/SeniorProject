from django.conf.urls import include, url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('breathe/', views.breathe, name='breathe'),
    path('machines_view/', views.machines_view, name='machines_view'),
    path('machines_view_Arm/', views.machines_view_Arm, name='machines_view_Arm'),
    path('machines_view_Leg/', views.machines_view_Leg, name='machines_view_Leg'),
    path('machines_view_Cardio/', views.machines_view_Cardio, name='machines_view_Cardio'),
    path('machines_view_Abs/', views.machines_view_Abs, name='machines_view_Abs'),
    path('plan/', views.plan_main, name='plan_main'),
    path('plan/new/', views.plan, name='plan'),
    path('workout/', views.workout, name='workout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('machines/', views.machines, name='machines'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('login/', views.login, name='login'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", views.register, name="register"),

]

