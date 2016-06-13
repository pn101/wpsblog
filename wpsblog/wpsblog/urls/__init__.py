from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib import admin

from wpsblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^news/$', news, name='news'),

    url(r'^', include('wpsblog.urls.auth', namespace='auth')),

    url(r'^policy/', include('wpsblog.urls.policy', namespace='policy')),

    url(r'^naver/posts/$', naver_posts_list, name='naver_posts_list'),

    url(r'^posts/', include('wpsblog.urls.posts', namespace='posts')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
