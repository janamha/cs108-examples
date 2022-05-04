# File: forms.py
# your name: Jana Mikaela Aguilar
# your email: janamha@bu.edu
# Description: Where you create HTML forms

from django import forms
from .models import Dancer, Choreographer, Room, Dance, Suggestion

class CreateDanceForm(forms.ModelForm):
    '''A form to create a Dance object.'''

    class Meta:
        '''additional data about this form'''
        model = Dance # which model to create
        fields = ['song', 'image'] # which fields to create

class CreateDancerForm(forms.ModelForm):
    '''A form to create a Dancer object.'''

    class Meta:
        '''additional data about this form'''
        model = Dancer # which model to create
        fields = ['first_name', 'last_name', 'level', 'email', 'dance'] # which fields to create


class CreateChoreographerForm(forms.ModelForm):
    '''A form to create a Choreographer object.'''

    class Meta:
        '''additional data about this form'''
        model = Choreographer # which model to create
        fields = ['first_name', 'last_name', 'email'] # which fields to create

class CreateRoomForm(forms.ModelForm):
    '''A form to create a Room object.'''

    class Meta:
        '''additional data about this form'''
        model = Room # which model to create
        fields = ['number', 'dance', 'choreographer'] # which fields to create

class UpdateDancerForm(forms.ModelForm):
    '''A form to update an existing Dancer object.'''

    class Meta:
        '''additional data about this form'''
        model = Dancer # which model to create
        fields = ['level', 'email'] # which fields to update

class UpdateRoomForm(forms.ModelForm):
    '''A form to update an existing Room object.'''

    class Meta:
        '''additional data about this form'''
        model = Room # which model to create
        fields = ['dance', 'choreographer'] # which fields to update

class LeaveSuggestionForm(forms.ModelForm):
    '''A form to leave a suggestion.'''

    class Meta:
        '''additional data about this form'''
        model = Suggestion # which model to create
        fields = ['name', 'ballet'] # which fields to update
