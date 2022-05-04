from django.shortcuts import render

from ast import Delete
import profile
from .models import Choreographer, Dancer, Dance, Room
from .forms import CreateDanceForm, CreateDancerForm, CreateChoreographerForm, CreateRoomForm, UpdateDancerForm, UpdateRoomForm, LeaveSuggestionForm
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse
import random

# Create your views here.
class ShowModelDirectory(ListView):
    '''Create a subclass of ListView to display all dancers.'''
    model = Dance
    template_name = 'project/home.html'
    context_object_name = 'dances2' # how to find the data in the template file

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowModelDirectory, self).get_context_data(**kwargs)
        # create a new SuggestionForm, and add it into the context dictionary
        form = LeaveSuggestionForm() 
        context['suggestion_form'] = form
        # return this context dictionary
        return context

class ShowAllDancersView(ListView):
    '''Create a subclass of ListView to display all dancers.'''

    model = Dancer # retrieve objects of type Dancer from the database
    template_name = 'project/show_all_dancers.html'
    context_object_name = 'dancers' # how to find the data in the template file

class ShowDancerPageView(DetailView):
    '''Create a subclass of DetailView to display the info of one profile.'''
    model = Dancer # retrieve objects of type Profile from the database
    template_name = 'project/show_dancer_profile.html'
    context_object_name = 'dancer' # how to find the data in the template file

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowDancerPageView, self).get_context_data(**kwargs)
        return context

class ShowAllChoreographersView(ListView):
    '''Create a subclass of ListView to display all choreographers.'''

    model = Choreographer # retrieve objects of type Choreographer from the database
    template_name = 'project/show_all_choreographers.html'
    context_object_name = 'choreographers' # how to find the data in the template file

class ShowAllDances(ListView):
    '''Create a subclass of ListView to display all choreographers.'''

    model = Dance # retrieve objects of type Dance from the database
    template_name = 'project/show_all_dances.html'
    context_object_name = 'dances' # how to find the data in the template file


class ShowAllRooms(ListView):
    '''Create a subclass of ListView to display all rooms.'''

    model = Room # retrieve objects of type Rpp, from the database
    template_name = 'project/show_all_rooms.html'
    context_object_name = 'rooms' # how to find the data in the template file

class ShowDanceView(DetailView):
    '''Create a subclass of DetailView to display the info of one dance.'''
    model = Dance # retrieve objects of type Profile from the database
    template_name = 'project/show_dance_profile.html'
    context_object_name = 'dance' # how to find the data in the template file

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowDanceView, self).get_context_data(**kwargs)
        return context
        
class CreateDanceView(CreateView):
    '''Create a new Dance object and store it in the database.'''

    model = Dance # which model to create
    form_class = CreateDanceForm # which form to use to create the Profile
    template_name = "project/create_dance_form.html" # delegate the dispay to this template

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the create.'''
 
        return reverse('show_all_dances')

class CreateDancerView(CreateView):
    '''Create a new Dancer object and store it in the database.'''

    model = Dancer # which model to create
    form_class = CreateDancerForm # which form to use to create the Profile
    template_name = "project/create_dancer_form.html" # delegate the dispay to this template

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the create.'''
 
        return reverse('show_all_dancers')


class CreateChoreographerView(CreateView):
    '''Create a new Choreographer object and store it in the database.'''

    model = Choreographer # which model to create
    form_class = CreateChoreographerForm # which form to use to create the Profile
    template_name = "project/create_choreographer_form.html" # delegate the dispay to this template

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the create.'''
 
        return reverse('show_all_choreographers')


class CreateRoomView(CreateView):
    '''Create a new Room object and store it in the database.'''

    model = Room # which model to create
    form_class = CreateRoomForm # which form to use to create the Profile
    template_name = "project/create_room_form.html" # delegate the dispay to this template

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the create.'''
 
        return reverse('show_all_rooms')

class ShowRoomPageView(DetailView):
    '''Create a subclass of DetailView to display the info of one room.'''
    model = Room # retrieve objects of type Profile from the database
    template_name = 'project/show_room_profile.html'
    context_object_name = 'room' # how to find the data in the template file

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowRoomPageView, self).get_context_data(**kwargs)
        return context

class UpdateDancerView(UpdateView):
    '''Update an existing Profile object and store it in the database.'''

    model = Dancer # which model to create
    form_class = UpdateDancerForm # which form to use to create the Profile
    template_name = "project/update_dancer_form.html" # delegate the display to this template


class UpdateRoomView(UpdateView):
    '''Update an existing Profile object and store it in the database.'''

    model = Room # which model to create
    form_class = UpdateRoomForm # which form to use to create the Profile
    template_name = "project/update_room_form.html" # delegate the display to this template

class DeleteDanceView(DeleteView):
    '''A view to delete a dancee and remove it from the database.'''

    template_name = "project/delete_dance_form.html"
    queryset = Dance.objects.all()

    def get_object(self):
        '''Return Status Message object.'''
		    # read the URL data values into variables
        dance_pk = self.kwargs['dance_pk']
        status = Dance.objects.get(pk=dance_pk)
        return status

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        context = super(DeleteDanceView, self).get_context_data(**kwargs)
        dance = Dance.objects.get(pk=self.kwargs['dance_pk'])
        context['dance'] = dance
        # return this context dictionary
        return context

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''
        dance_pk = self.kwargs['dance_pk']

        message = Dance.objects.filter(pk=dance_pk).first() # get one object from QuerySet
        
        # reverse to show the person page
        return reverse('show_all_dances')

def submit_suggestion(request):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':
        
        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = LeaveSuggestionForm(request.POST or None, request.FILES or None)
        print(form)
        if form.is_valid():

            # create the StatusMessage object with the data in the LeaveStatusSuggestionForm
            suggestion = form.save(commit=False) # don't commit to database yet

            # now commit to database
            suggestion.save()
            print(suggestion.ballet)
        else:
            print(form)
    
    # redirect the user to the show_profile_page view
    url = reverse('base')
    return redirect(url)