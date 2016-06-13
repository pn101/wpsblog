from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostDeleteView(PostBaseView, LoginRequiredMixin, DeleteView):
    template_name = 'posts/deletepost.html'
    success_url = reverse_lazy('posts:list')
