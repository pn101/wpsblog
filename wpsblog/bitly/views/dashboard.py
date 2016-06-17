from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import BitLinkBaseView


class BitLinkDashboardView(BitLinkBaseView, LoginRequiredMixin, ListView):
    template_name = 'dashboard.html'
    context_object_name = 'bitlink'

    def get_queryset(self):
        bitlink = self.model.objects.get(
                shorten_hash=self.kwargs.get('shorten_hash'),
        )
        return bitlink

    def get_context_data(self, **kwargs):
        context = super(BitLinkDashboardView, self).get_context_data(**kwargs)
        context['site_name'] = 'Dashboard View'
        return context
