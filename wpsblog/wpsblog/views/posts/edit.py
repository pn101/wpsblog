from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostEditView(PostBaseView, LoginRequiredMixin, UpdateView):
    template_name = 'posts/edit.html'
    fields = ['title', 'content', 'image']
