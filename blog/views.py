from typing import Any
from uuid import uuid4
from django.db.models.query import QuerySet
from django.contrib.auth.decorators import login_required
from django.forms.models import BaseModelForm
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from . models import Blog, Comment, Like
from .forms import CommentForm


# Create your views here.


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['blog_title', 'blog_content', 'blog_image']
    template_name = 'blog/write_blog.html'

    def form_valid(self, form: BaseModelForm):
        user_blog = form.save(commit=False)
        user_blog.author = self.request.user
        title = user_blog.blog_title
        user_blog.slug = title.replace(' ', '_')+"-"+str(uuid4())
        user_blog.save()
        return HttpResponseRedirect(reverse('blog:blog_list'))


class BlogList(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().order_by('-publish_at')


@login_required
def blog_details(request, id):
    blog = Blog.objects.get(pk=id)
    comment_form = CommentForm()
    all_comment = Comment.objects.filter(blog=blog)
    already_like = Like.objects.filter(user=request.user, blog=blog)
    if already_like:
        liked = True
    else:
        liked = False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('blog:details', kwargs={'id': id}))
    return render(request, 'blog/blog_details.html', context={'blog': blog, 'comment_form': comment_form, 'all_comment': all_comment, 'liked': liked})


class AuthorDetails(DetailView):
    model = User
    template_name = 'login/profile_details.html'
    context_object_name = 'author'


@login_required
def like(request, pk):
    current_user = request.user
    blog = Blog.objects.get(pk=pk)
    already_liked = Like.objects.filter(user=current_user, blog=blog)
    if not already_liked:
        like_post = Like(user=current_user, blog=blog)
        like_post.save()
    return HttpResponseRedirect(reverse('blog:details', kwargs={'id': blog.pk}))


@login_required
def unlike(request, pk):
    current_user = request.user
    blog = Blog.objects.get(pk=pk)
    already_like = Like.objects.filter(user=current_user, blog=blog)
    if already_like:
        already_like.delete()
    return HttpResponseRedirect(reverse('blog:details', kwargs={'id': blog.pk}))


class MyBlog(LoginRequiredMixin, TemplateView):
    template_name = 'blog/myblog.html'


class EditBlog(LoginRequiredMixin, UpdateView):
    template_name = 'blog/editblog.html'
    model = Blog
    fields = ['blog_title', 'blog_content', 'blog_image']

    def get_success_url(self):
        return reverse_lazy('blog:details', kwargs={'id': self.object.pk})


class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/delete.html'

    def get_success_url(self):
        return reverse_lazy('blog:myblog')
