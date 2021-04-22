from django.contrib import admin

# Register your models here.
from .models import Profile, Machines, Workout, Exercise


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'rep_type')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Machines, MachineAdmin)


