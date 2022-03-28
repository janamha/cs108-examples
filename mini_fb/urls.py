##### mini_fb/urls.py #####

from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView # our view class definition 

urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'), # generic class-based view
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # show one quote
]