from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .base import BitLinkBaseView


class BitLinkRedirectView(BitLinkBaseView, LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        bitlink = get_object_or_404(
                self.request.user.bitlink_set.all(),
                shorten_hash=self.kwargs.get('shorten_hash')
        )

        return bitlink.original_url
