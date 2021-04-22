from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Machines


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')


admin.site.register(Profile, ProfileAdmin)


class MachineAdmin(admin.ModelAdmin):
    list_display = ('name','type','rep_type')

admin.site.register(Machines, MachineAdmin)


