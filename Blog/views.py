from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'EFE',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 23, 2024'
    },
    {
        'author': 'David',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 24, 2024'
    },
    
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'Blog/home.html', context)

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})
