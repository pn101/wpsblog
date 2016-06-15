from django.views.generic.base import RedirectView

from bitly.models import BitLink

class BitLinkRedirectView(RedirectView):

    def get(self, request, *args, **kwargs):
        bitlink = Bitlink.objects.get(shorten_hash='shorten_hash')
        return redirect(bitlink.original_url)
