from django.shortcuts import render

from wpsblog.models import Post


def list(request):
    search = request.GET.get('search')
    post_list = Post.objects.all()
    if search:
        post_list = Post.objects.filter(title=search)

    return render(
            request,
            'posts/list.html',
            {
                'site_name': 'Blog List',
                'post_list': post_list,
            }
    )
