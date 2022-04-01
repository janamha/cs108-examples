# File: views.py
# your name: Jana Mikaela Aguilar
# your email: janamha@bu.edu
# Description: Creates views to display profiles

from quotes.forms import UpdateQuoteForm
from .models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import CreateProfileForm, UpdateProfileForm

class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all profiles.'''

    model = Profile # retrieve objects of type Profile from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' # how to find the data in the template file


class ShowProfilePageView(DetailView):
    '''Create a subclass of DetailView to display the info of one profile.'''
    model = Profile # retrieve objects of type Profile from the database
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile' # how to find the data in the template file

class CreateProfileView(CreateView):
    '''Create a new Quote object and store it in the database.'''

    model = Profile # which model to create
    form_class = CreateProfileForm # which form to use to create the Profile
    template_name = "mini_fb/create_profile_form.html" # delegate the dispay to this template

class UpdateProfileView(UpdateView):
    '''Update an existing Quote object and store it in the database.'''

    model = Profile # which model to create
    form_class = UpdateProfileForm # which form to use to create the Quote
    template_name = "mini_fb/update_profile_form.html" # delegate the display to this template