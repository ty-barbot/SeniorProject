from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('breathe/', views.breathe, name='breathe'),
    path('plan/', views.plan, name='plan'),
    path('workout/', views.workout, name='workout'),
    path('profile/', views.profile, name='profile'),
    path('machines/', views.machines, name='machines'),
]
