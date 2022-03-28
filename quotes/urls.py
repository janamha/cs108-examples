##### quotes/urls.py #####

from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuoteView, PersonPageView # our view class definition 

urlpatterns = [
    # map the URL (empty string) to the view
    path('all', HomePageView.as_view(), name='all'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # show one quote
    path('', RandomQuoteView.as_view(), name='random'),  # show one quote at random
    path('person/<int:pk>', PersonPageView.as_view(), name="person"), ## NEW URL TO SHOW PERSON PAGE
]