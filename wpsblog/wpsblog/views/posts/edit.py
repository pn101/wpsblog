from django.shortcuts import render

from wpsblog.models import Post


def edit(request, post_id):
    return render(
            request,
            'posts/edit.html',
            {
                'site_name': 'Edit Blog',
                'post': Post.objects.get(id=post_id),
            }
    )
