from .models import Organization, Activity
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class OrganizationView(ListView):
    model = Organization
    template_name = 'volunteering/organization.html'
    context_object_name = 'organization_list'


class CreateOrganization(CreateView):
    model = Organization
    fields = '__all__'


class DetailOrganization(DetailView):
    model = Organization
    template_name = 'volunteering/organization_profile.html'

    success_url = reverse_lazy('volunteering:activity_form')


class CreateActivity(CreateView):
    model = Activity
    fields = '__all__'


class DetailActivity(DetailView):
    model = Activity
    template_name = 'volunteering/organization_activity.html'
    context_object_name = 'activity_list'
