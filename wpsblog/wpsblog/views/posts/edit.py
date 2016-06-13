from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from wpsblog.models import Post


class PostEditView(LoginRequiredMixin, TemplateView):
    template_name = 'posts/edit.html'
