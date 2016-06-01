from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_posts_list(request):
    keyword = request.GET.get('keyword')
    naver_post_list = NaverPost.objects.all()
    if keyword:
        naver_post_list = [
            post for post in naver_post_list if keyword in post.title
        ]
    return render(
            request,
            'naver_posts/naver_posts_list.html',
            {
                'naver_posts': naver_post_list,
            }
    )
