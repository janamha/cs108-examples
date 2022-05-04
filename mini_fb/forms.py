# File: forms.py
# your name: Jana Mikaela Aguilar
# your email: janamha@bu.edu
# Description: Where you create HTML forms

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create a Profile object.'''

    class Meta:
        '''additional data about this form'''
        model = Profile # which model to create
        fields = ['first_name', 'last_name', 'city', 'email', 'image_url'] # which fields to create

class UpdateProfileForm(forms.ModelForm):
    '''A form to update an existing Profile object.'''

    class Meta:
        '''additional data about this form'''
        model = Profile # which model to create
        fields = ['first_name', 'last_name', 'city', 'email', 'image_url'] # which fields to update

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create a Status Message.'''

    image = forms.ImageField(required=False)
    
    class Meta:
        '''additional data about this form'''
        model = StatusMessage # which model to create
        fields = ['message', 'image'] # which fields to create