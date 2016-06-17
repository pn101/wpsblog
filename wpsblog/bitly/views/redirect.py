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

        bitlinklog = bitlink.bitlinklog_set.create(
                http_referer=self.request.META.get('HTTP_REFERER'),
                http_user_agent=self.request.META.get('HTTP_USER_AGENT'),
                remote_addr=self.request.META.get('REMOTE_ADDR'),
                http_meta_json=str(self.request.META),
        )

        return bitlink.original_url
