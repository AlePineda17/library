from django.urls import path
from . import views

app_name = 'volunteering'
urlpatterns = [
    path('volunteering/organization/', views.OrganizationView.as_view(), name='organization'),
    path('volunteering/organization_form/', views.CreateOrganization.as_view(), name='organization_form'),
    path('volunteering/<int:pk>/organization_profile/', views.DetailOrganization.as_view(), name='organization_profile'),
    path('volunteering/activity_form/', views.CreateActivity.as_view(), name='activity_form'),
    path('volunteering/<int:pk>/organization_activity/', views.DetailActivity.as_view(), name='organization_activity'),
]
