from django.contrib import admin


# Register your models here.
from .models import Dancer, Choreographer, Room, Dance

admin.site.register(Dancer)
admin.site.register(Choreographer)
admin.site.register(Room)
admin.site.register(Dance)