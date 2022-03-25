# File: models.py
# your name: Jana Mikaela Aguilar
# your email: janamha@bu.edu
# Description: Where you create models for your app and stirng representation

from django.db import models

class Profile(models.Model):
    '''Encapsulate the idea of a Profile.'''

    # data attributes of a profile:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)   
    image_url = models.URLField(blank=True)


    def __str__(self):
        '''Return a string representation of this Profile object.'''
        return f'"{self.first_name}" - {self.last_name} - {self.city} - {self.email}'