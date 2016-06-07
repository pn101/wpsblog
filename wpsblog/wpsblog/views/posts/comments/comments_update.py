from django.shortcuts import redirect

from wpsblog.models import Post, Comment


def comments_update(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    content = request.POST.get('content')
    comment.content = content
    comment.save()

    return redirect(comment)
