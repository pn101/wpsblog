from django.views.generic import View

from wpsblog.models import Comment


class CommentBaseView(View):
    model = Comment
