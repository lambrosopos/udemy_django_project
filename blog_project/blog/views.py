from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.views import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, edit, ListView, DetailView, CreateView, UpdateView, 
                                    DeleteView)

# Blog app
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'


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



# Comment Views
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            # Temporarily save the CommentForm to comment without commit
            comment = form.save(commit=False)

            # After adding on the post value save
            comment.post = post
            comment.save()

            return redirect('post_detail', pk = post.pk)
    
    # Someone haven't filled out the comment form
    else:
        form = CommentForm()
    
    return render(request, 'blog/comment_form.html', context={'form':form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk

    comment.delete()
    return redirect('post_detail', pk=post_pk)