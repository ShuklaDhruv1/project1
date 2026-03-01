from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import SpaceTopic

def topic_home(request):
    topics = SpaceTopic.objects.all()
    return render(request, 'spacepedia/topic_home.html', {'topics': topics})

def topic_detail(request, slug):
    topic = get_object_or_404(SpaceTopic, slug=slug)
    return render(request, 'spacepedia/topic_detail.html', {'topic': topic})