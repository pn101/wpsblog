from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import BitLinkBaseView


class BitLinkCreateView(BitLinkBaseView, LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    fields = [
        'content',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BitLinkCreateView, self).form_valid(form)
