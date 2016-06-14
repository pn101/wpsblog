from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from wpsblog.models import Post
from .base import CommentBaseView


class PostCommentCreateView(CommentBaseView, LoginRequiredMixin, CreateView):
    fields = [
        'content',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(
                id=self.kwargs.get('post_id')
        )

        return super(PostCommentCreateView, self).form_valid(form)
