from django.db import models
from django.urls import reverse

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=32)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('volunteering:organization')
