from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('user_form/', views.CreateUser.as_view(), name='user_form'),
]
