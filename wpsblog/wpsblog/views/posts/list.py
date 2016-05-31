from django.shortcuts import render

from wpsblog.models import Post


def list(request):
    return render(
            request,
            'posts/list.html',
            {
                'site_name': 'Blog List',
                'post_list': Post.objects.all()}
    )
