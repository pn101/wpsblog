from django.views.generic import View

from bitly.models.bitly import BitLink


class BitLinkBaseView(View):
    model = BitLink
