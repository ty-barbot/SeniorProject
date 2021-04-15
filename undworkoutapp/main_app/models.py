from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    TODO:
        - get rid of username and password fields
        - change height and weight to integer, maybe separate height to feet and inches
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('Non-binary', 'Non-binary'),
        ('Prefer not to say', 'Prefer not to say'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, blank=True, null=False)
    password = models.CharField(max_length=30, blank=True, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    birth_date = models.DateField(null=True, blank=True)
    height = models.CharField(max_length=20, blank=True, null=False)
    weight = models.CharField(max_length=20, blank=True, null=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def age(self):
        import datetime
        return int((datetime.date.today() - self.birth_date).days / 365.25)

    def __str__(self):
        return self.username


class Machine(models.Model):
    TYPE_CHOICES = (
        ('Arm', 'Arm'),
        ('Leg', 'Leg'),
        ('Cardio', 'Cardio'),
    )
    REP_CHOICES = (
        ('Sets', 'Sets'),
    )
    name = models.CharField(max_length=50, blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False, choices=TYPE_CHOICES)
    rep_type = models.CharField(max_length=20, blank=False, null=False, choices=REP_CHOICES)

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    workout = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True)
    sets = models.CharField(max_length=50, blank=False, null=False) # maybe array?

    def __str__(self):
        return self.name


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
