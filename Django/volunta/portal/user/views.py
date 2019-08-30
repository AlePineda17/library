# from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User


class CreateUser(CreateView):
    model = User
    fields = '__all__'
