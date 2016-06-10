from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from wpsblog.models import Post, Comment


@login_required
def comments_create(request, post_id):
    content = request.POST.get('content')
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.create(
            content=content,
    )
    return redirect(comment)
