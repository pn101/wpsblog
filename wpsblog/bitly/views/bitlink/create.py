from django.views.generic.edit import CreateView
import random

from bitly.models import BitLink


class BitLinkCreateView(CreateView):
    template_name = 'bitlink/create.html'
    fields = ['original_url', 'shorten_url']

    def form_valid(self, form):
        form.instance.shorten_url = random.randint(1, 999999)
        return super(BitLinkCreateView, self).form_valid(form)
