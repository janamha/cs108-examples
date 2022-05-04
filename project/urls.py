from tokenize import Name
from django.urls import path

from .views import CreateDanceView, ShowAllDancersView, ShowAllChoreographersView, ShowDancerPageView, ShowModelDirectory, ShowAllDances, ShowDanceView, ShowAllRooms, CreateRoomView, CreateDancerView, CreateChoreographerView, UpdateDancerView, UpdateRoomView, DeleteDanceView, ShowRoomPageView, submit_suggestion # our view class definition 

urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowModelDirectory.as_view(), name='base'), 
    path('dancers', ShowAllDancersView.as_view(), name='show_all_dancers'), 
    path('profile/<int:pk>', ShowDancerPageView.as_view(), name='show_dancer_profile'),
    path('create_dancer_form', CreateDancerView.as_view(), name='create_dancer_form'),
    path('profile/<int:pk>/update', UpdateDancerView.as_view(), name="update_dancer_form"), 
    path('choreographers', ShowAllChoreographersView.as_view(), name='show_all_choreographers'), 
    path('create_choreographer_form', CreateChoreographerView.as_view(), name='create_choreographer_form'),
    path('dances', ShowAllDances.as_view(), name='show_all_dances'),
    path('dance/<int:pk>', ShowDanceView.as_view(), name='show_dance_profile'),
    path('create_dance_form', CreateDanceView.as_view(), name='create_dance_form'),
    path('dance/<int:dance_pk>/delete_dance', DeleteDanceView.as_view(), name="delete_dance"), 
    path('rooms', ShowAllRooms.as_view(), name='show_all_rooms'),
    path('room/<int:pk>', ShowRoomPageView.as_view(), name='show_room_profile'),
    path('create_room_form', CreateRoomView.as_view(), name='create_room_form'),
    path('room/<int:pk>/update', UpdateRoomView.as_view(), name='update_room_form'),
    path('submit_suggestion', submit_suggestion, name='leave_suggestion'), 

]