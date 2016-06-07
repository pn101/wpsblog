from django.shortcuts import render

from wpsblog.models import Post


def list(request):
    search = request.GET.get('search')
    post_list = Post.objects.public

    if search:
        post_list = [
                post for post in post_list if search in post.title
        ]

    return render(
            request,
            'posts/list.html',
            {
                'site_name': 'Blog List',
                'post_list': post_list,
            }
    )
