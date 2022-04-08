# File: urls.py
# your name: Jana Mikaela Aguilar
# your email: janamha@bu.edu
# Description: direct URL requests to view functions


from tokenize import Name
from django.urls import path
from .views import DeleteStatusMessageView, ShowAllProfilesView, ShowPossibleFriendsView, ShowProfilePageView, CreateProfileView, ShowsNewsFeedView, UpdateProfileView, post_status_message, add_friend # our view class definition 

urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'), # generic class-based view
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # show one profile
    path('create_profile', CreateProfileView.as_view(), name='create_profile'), ## NEW
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"), 
    path('profile/<int:pk>/post_status', post_status_message, name="post_status"), 
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name="delete_status"), 
    path('profile/<int:pk>/news_feed', ShowsNewsFeedView.as_view(), name='news_feed'),
    path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name='show_possible_friends'),
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', add_friend, name='add_friend')
]