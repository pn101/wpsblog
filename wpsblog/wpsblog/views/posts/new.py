from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostNewView(PostBaseView, LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostNewView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostNewView, self).get_context_data(**kwargs)
        context['site_name'] = 'Create FastBlog'
        return context
