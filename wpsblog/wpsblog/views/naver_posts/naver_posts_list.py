from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_posts_list(request):
    keyword = request.GET.get('keyword')
    query = request.GET.get('query')
    naver_post_list = NaverPost.objects.all()

    if keyword:
        naver_post_list = naver_post_list.filter(keyword=keyword)

    if query:
        naver_post_list = naver_post_list.filter(title__contains=query)

    return render(
            request,
            'naver_posts/naver_posts_list.html',
            {
                'keyword': keyword,
                'query': query,
                'naver_posts': naver_post_list,
            }
    )
