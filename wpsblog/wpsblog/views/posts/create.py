from django.views.generic.edit import CreateView

from wpsblog.models import Post


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'content', 'image']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(PostCreateView, self).form_valid(form)
