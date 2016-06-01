from django.conf.urls import url, include
from django.contrib import admin

from wpsblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^news/$', news, name='news'),
    url(r'^policy/', include('wpsblog.urls.policy', namespace='policy')),

    url(r'^naver/posts/$', naver_posts_list, name='naver_posts_list'),

    url(r'^posts/', include('wpsblog.urls.posts', namespace='posts')),
]
