from django.contrib import admin
# File: admin.py
# your name: Jana Mikaela Aguilar
# your email: janamha@bu.edu
# Description: Register models here

from .models import Profile, StatusMessage
admin.site.register(Profile)
admin.site.register(StatusMessage)