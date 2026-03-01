from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from blog.models import Post
from spacepedia.models import SpaceTopic
from django.db.models import Q

def home(request):
    return render(request, 'core/home.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please login.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def search(request):
    q = request.GET.get('q', '').strip()
    posts = topics = []
    if q:
        posts = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
        topics = SpaceTopic.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'core/search.html', {'q': q, 'posts': posts, 'topics': topics})