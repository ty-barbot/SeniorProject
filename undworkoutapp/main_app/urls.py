from django.conf.urls import include, url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('breathe/', views.breathe, name='breathe'),
    path('machines_view/', views.machines_view, name='machines_view'),
    path('plan/', views.plan_main, name='plan_main'),
    path('plan/new/', views.plan, name='plan'),
    path('workout/', views.workout, name='workout'),
    path('profile/', views.profile, name='profile'),
    path('machines/', views.machines, name='machines'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('login/', views.login, name='login'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", views.register, name="register"),

]

