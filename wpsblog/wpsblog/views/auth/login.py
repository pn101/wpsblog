from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next_page')
        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            if next_page:
                return redirect(next_page)
            return redirect(reverse('auth:mypage'))
        return redirect(reverse('auth:login'))

    return render(
            request,
            'auth/login.html',
            {
                'site_name': 'Login',
                'author': 'Philip Nam',
            }
    )
