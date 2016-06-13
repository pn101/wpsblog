from django.views.generic.list import ListView

from wpsblog.models import Post
from .base import PostBaseView


class PostListView(PostBaseView, ListView):
    template_name = 'posts/list.html'
    context_object_name = 'post_list'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('per', 5)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['site_name'] = 'FastBlog'
        return context
