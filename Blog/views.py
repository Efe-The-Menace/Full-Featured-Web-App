from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog-home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user   
        return super().form_valid(form)



def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})