from django.db import models

# Create your models here.
class Dancer(models.Model):
    '''Encapsulate the idea of a Dancer.'''

    # data attributes of a Dancer:
    id = models.BigIntegerField(blank=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    level = models.BigIntegerField(blank=True)
    email = models.TextField(blank=True)
    dance = models.ForeignKey('Dance', on_delete=models.CASCADE)

class Choreographer(models.Model):
    '''Encapsulate the idea of a Chorepytographer.'''

    # data attributes of a Choreographer:
    id = models.BigIntegerField(blank=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email = models.TextField(blank=True)
class Room(models.Model):
    '''Encapsulate the idea of a Choreographer.'''

    # data attributes of a Room:
    number = models.BigIntegerField(blank=True)
    Dance = models.ForeignKey('Dance', on_delete=models.CASCADE)
    choreographer = models.ForeignKey('Choreographer', on_delete=models.CASCADE)

class Dance(models.Model):
    '''Encapsulate the idea of a Dance.'''

    # data attributes of a dance: 
    id = models.BigIntegerField(blank=True)
    song = models.TextField(blank=True)
