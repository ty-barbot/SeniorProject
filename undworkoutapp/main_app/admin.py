from django.contrib import admin

# Register your models here.
from .models import Profile, Machine, Workout, Exercise


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')


class MachineAdmin(admin.ModelAdmin):
    list_display = ('name',)


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise, ExerciseAdmin)
