from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


def index(request):
    dic = {}
    return HttpResponseRedirect(reverse('blog:blog_list'))
