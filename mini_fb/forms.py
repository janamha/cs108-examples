from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):

    # first_name = forms.CharField(label="First Name", required=True)
    # last_name = forms.CharField(label="Last Name", required=True)
    # city = forms.CharField(label="City", required=True)
    # email = forms.CharField(label="First Name", required=True)
    # image_url = forms.URLField(label="Image URL", required=True)

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
