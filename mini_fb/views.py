# File: views.py
# your name: Jana Mikaela Aguilar
# your email: janamha@bu.edu
# Description: Creates views to display profiles

from .models import Profile
from django.views.generic import ListView

class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all profiles.'''

    model = Profile # retrieve objects of type Profile from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' # how to find the data in the template file