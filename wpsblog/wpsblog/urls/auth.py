from django.conf.urls import url

from wpsblog.views.auth import *


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^mypage/$', MyPageView.as_view(), name='mypage'),
]
