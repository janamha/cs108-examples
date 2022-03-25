##### quotes/models.py #####

from django.db import models

class Quote(models.Model):
    '''Encapsulate the idea of a quote (i.e., text).'''

    # data attributes of a quote:
    text = models.TextField(blank=True)
    author = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this Quote object.'''
        return f'"{self.text}" - {self.author}'