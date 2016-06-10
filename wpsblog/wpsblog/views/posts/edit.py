from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from wpsblog.models import Post


@login_required
def edit(request, post_id):
    return render(
            request,
            'posts/edit.html',
            {
                'site_name': 'Edit Blog',
                'post': Post.objects.get(id=post_id),
                'author': 'Philip Nam',
            }
    )
