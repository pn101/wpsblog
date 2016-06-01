from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_posts_list(request):
    return render(
            request,
            'naver_posts/naver_posts_list.html',
            {
                'naver_posts': NaverPost.objects.all()
            }
    )
