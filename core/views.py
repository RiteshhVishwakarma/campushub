from django.shortcuts import render
from posts.models import Post


def home(request):
    """Home page view"""
    # Get latest 8 active posts
    latest_posts = Post.objects.filter(is_active=True).select_related('user')[:8]
    return render(request, 'core/home.html', {'latest_posts': latest_posts})


def about(request):
    """About page view"""
    return render(request, 'core/about.html')
