from django.db import models
from django.urls import reverse

# Create your models here.
class Dancer(models.Model):
    '''Encapsulate the idea of a Dancer.'''

    # data attributes of a Dancer:
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    level = models.BigIntegerField(blank=True)
    email = models.TextField(blank=True)
    dance = models.ForeignKey('Dance', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def get_absolute_url(self):
        '''Return a URL to display this dancer object.'''

        return reverse("show_dancer_profile", kwargs={"pk": self.pk})

    def __str__(self):
        '''Return a string representation of this Dancer object.'''
        return f'{self.first_name} - {self.last_name}'

class Choreographer(models.Model):
    '''Encapsulate the idea of a Choreographer.'''

    # data attributes of a Choreographer:
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email = models.TextField(blank=True)

    def __str__(self):
        '''Return a string representation of this Choreographer object.'''
        return f'{self.first_name} - {self.last_name}'

class Room(models.Model):
    '''Encapsulate the idea of a Choreographer.'''

    # data attributes of a Room:
    number = models.BigIntegerField(blank=True)
    dance = models.ForeignKey('Dance', on_delete=models.CASCADE)
    choreographer = models.ForeignKey('Choreographer', on_delete=models.CASCADE)
    location = models.TextField(blank=True)

    def get_absolute_url(self):
        '''Return a URL to display this dancer object.'''

        return reverse("show_all_rooms")

    def __str__(self):
        '''Return a string representation of this Dance object.'''
        return f'{self.number} - {self.dance}'

class Dance(models.Model):
    '''Encapsulate the idea of a Dance.'''

    # data attributes of a dance: 
    id = models.AutoField(primary_key=True)
    song = models.TextField(blank=True)
    image = models.URLField(blank=True)
    spotify = models.URLField(blank=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        '''Return a string representation of this Dance object.'''
        return f'{self.song}'

class Suggestion(models.Model):
    """Encapsulates the idea of a suggestion"""
    # data attributes of a suggestion:

    name = models.TextField(blank=True)
    timestamp = models.TimeField(auto_now=True)
    ballet = models.TextField(blank=True)

    def __str__(self):
        '''Return a string representation of this Suggestion object.'''
        return f'{self.timestamp} - {self.name}'