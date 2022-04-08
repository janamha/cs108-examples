# File: models.py
# your name: Jana Mikaela Aguilar
# your email: janamha@bu.edu
# Description: Where you create models for your app and stirng representation

import profile
from django.db import models
from django.urls import reverse

class Profile(models.Model):
    '''Encapsulate the idea of a Profile.'''

    # data attributes of a profile:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)   
    image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def get_status_messages(self):
        '''Return all status messages for this Profile.'''

        # use the object manager to filter Status Messages by this person's pk:
        return StatusMessage.objects.filter(profile=self)

    def get_absolute_url(self):
        '''Return a URL to display this profile object.'''
        return reverse("show_profile_page", kwargs={"pk": self.pk})

    def get_friends(self):
        '''Return all friends for this Profile.'''

        return self.friends.all()

    def get_news_feed(self):
        '''Obtains and returns newsfeed items'''


        news = StatusMessage.objects.filter(profile__in=self.get_friends()).order_by("-timestamp")
        return news

    def get_friend_suggestions(self):
        'obtain and return a QuerySet of all Profile that could be added as friends.'

        # returns profiles
        possible_friends = friend_suggestions = Profile.objects.exclude(pk__in=self.friends.all()).exclude(pk=self.pk)
        return possible_friends

    def __str__(self):
        '''Return a string representation of this Profile object.'''
        return f'"{self.first_name}" - {self.last_name} - {self.city} - {self.email}'

class StatusMessage(models.Model):
    "Encapsulate the idea of a Facebook Status Message"
    
    # data attributes of a message:
    timestamp = models.TimeField(auto_now=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        '''Return a string representation of this Status Message object.'''
        return f'"{self.timestamp}" - {self.message} - {self.profile} - {self.image}'
