from django.conf.urls import url, include
from django.contrib import admin

from wpsblog.views.posts import *


urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^(?P<post_id>\d+)/$', detail, name='detail'),
    url(r'^new/$', new, name='new'),
    url(r'^create/$', create, name='create'),
    url(r'^(?P<post_id>\d+)/edit/$', edit, name='edit'),
    url(r'^(?P<post_id>\d+)/update/$', update, name='update'),
    url(r'^(?P<post_id>\d+)/delete/$', delete, name='delete'),
]
