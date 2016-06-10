from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def new(request):
    return render(
            request,
            'posts/new.html',
            {
                'site_name': 'New Post',
                'author': 'Philip Nam',
            }
    )
