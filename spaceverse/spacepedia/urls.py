from django.urls import path
from .views import topic_home, topic_detail

urlpatterns = [
    path('', topic_home, name='topic_home'),
    path('<slug:slug>/', topic_detail, name='topic_detail'),
]