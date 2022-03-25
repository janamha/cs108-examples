from django.db import models

# Create your models here.
##### mini_fb/ models.py #####

class Profile(models.Model):
    '''Encapsulate the idea of a quote by some author (i.e., text).'''

    # data attributes of a profile:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)   
    image_url = models.URLField(blank=True)


    def __str__(self):
        '''Return a string representation of this Profile object.'''
        return f'"{self.first_name}" - {self.last_name} - {self.city} - {self.email}'