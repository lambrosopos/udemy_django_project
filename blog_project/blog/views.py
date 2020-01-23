from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, edit, ListView, DetailView, CreateView, UpdateView, 
                                    DeleteView)

# Blog app
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    # Using a Mixin means mixing views...
    # In this case it is mixing login required with creating view

    # A required parameter for login mixin is login_url to redirect the user if not logged in
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    # Using a Mixin means mixing views...
    # In this case it is mixing login required with creating view

    # A required parameter for login mixin is login_url to redirect the user if not logged in
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    # You need the model which you wish to change
    model = Post

    # You don't want to activate success_url until actually validated
    # reverse_lazy([view name]) - check urls.py for names
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    # Basically an SQL command line (query line)
    # Filters for SQL commands (see docs for more detail)
    # You can basically do the same as SQL, look into models for exact names
    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True).order_by('created_at')
