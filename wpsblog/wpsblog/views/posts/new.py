from django.shortcuts import render


def new(request):
    return render(
            request,
            'posts/new.html',
            {
                'site_name': 'New Post',
                'author': 'Philip Nam',
            }
    )
