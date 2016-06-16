from django.conf.urls import url

from bitly.views.bitlink import *


urlpatterns = [
    url(r'^create/$', BitLinkCreateView.as_view(), name='create'),
    url(r'^(?P<shorten_hash>\w+)/$', BitLinkRedirectView.as_view(), name='redirect'),

]
