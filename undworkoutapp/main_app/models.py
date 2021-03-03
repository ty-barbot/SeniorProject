from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Machine Model
#   -name
#   -type/group
#   -sets (true/false?) or just reps
#
# Workout Model
#   -name
#   -date planned (optional)
#   -exercises (related model?)
#
# Exercise Model
#   -machine
#   -sets and reps
