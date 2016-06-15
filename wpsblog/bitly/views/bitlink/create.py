from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from hashids import Hashids

from .base import BitLinkBaseView


class BitLinkCreateView(BitLinkBaseView, LoginRequiredMixin, CreateView):
    template_name = 'bitlink.html'
    fields = [
        'original_url',
    ]
    success_url = reverse_lazy('auth:mypage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BitLinkCreateView, self).form_valid(form)
