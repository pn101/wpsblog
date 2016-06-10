from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from wpsblog.models import Post, Comment


@login_required
def comments_delete(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)
    comment.delete()

    return redirect(post)
