######## file: pages/urls.py ########
# description: direct URL requests to view functions

from django.urls import path
from .views import BasePageView, HomePageView, AboutPageView, SchedulePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('base', BasePageView.as_view(), name='base'),
    path('schedule', SchedulePageView.as_view(), name='schedule'),
]