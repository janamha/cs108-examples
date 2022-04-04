##### quotes/urls.py #####

from django.urls import path
from .views import *

urlpatterns = [
    # map the URL (empty string) to the view
    path('all', HomePageView.as_view(), name='all'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # show one quote
    path('', RandomQuoteView.as_view(), name='random'),  # show one quote at random
    path('person/<int:pk>', PersonPageView.as_view(), name="person"), ## NEW URL TO SHOW PERSON PAGE
    path('create_quote', CreateQuoteView.as_view(), name='create_quote'), ## NEW
    path('quote/<int:pk>/update', UpdateQuoteView.as_view(), name="update_quote"), 
    path('quote/<int:pk>/delete', DeleteQuoteView.as_view(), name="delete_quote"), # NEW
    path('person/<int:pk>/add_image', add_image, name="add_image"), ## NEW
]