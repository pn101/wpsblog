from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostNewView(PostBaseView, LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostNewView, self).form_valid(form)
