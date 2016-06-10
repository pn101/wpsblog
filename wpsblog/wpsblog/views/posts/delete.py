from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from wpsblog.models import Post


@login_required
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect(
            reverse('posts:list')
    )
