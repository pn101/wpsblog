from django.shortcuts import render

from wpsblog.models import Post


def detail(request, post_id):
    return render(
            request,
            'posts/detail.html',
            {
                'site_name': 'Blog Entry',
                'post': Post.objects.get(id=post_id),
                'author': 'Philip Nam',
            }
    )
