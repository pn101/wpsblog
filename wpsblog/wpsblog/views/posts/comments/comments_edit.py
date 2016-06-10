from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from wpsblog.models import Post, Comment


@login_required
def comments_edit(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    return render(
            request,
            'posts/comments_edit.html',
            {
                'site_name': 'Edit Comment',
                'post': post,
                'comment': comment,
                'author': 'Philip Nam',
            }
    )
