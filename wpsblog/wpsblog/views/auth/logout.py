from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def logout(request):
    auth_logout(request)
    return redirect(reverse('auth:login'))