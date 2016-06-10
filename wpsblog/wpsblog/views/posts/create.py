from django.shortcuts import redirect

from wpsblog.models import Post


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('image')

    post = request.user.post_set.create(
            title=title,
            content=content,
            image=image,
    )

    return redirect(post)
