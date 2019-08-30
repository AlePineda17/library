from django.db import models
from django.urls import reverse
from user.models import User


class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('volunteering:organization_profile', kwargs={'pk': self.pk})


class Activity(models.Model):
    TYPE_CHOICES = (
        (1, 'Health'),
        (2, 'Nutrition'),
        (3, 'Education'),
    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.IntegerField(choices=TYPE_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    place = models.CharField(max_length=150)
    requirements = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('volunteering:organization_activity', kwargs={'pk': self.pk})


class Subscription(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
