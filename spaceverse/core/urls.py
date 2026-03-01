from django.urls import path
from .views import home, signup, search

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('search/', search, name='search'),
]