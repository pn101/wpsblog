from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Comment(models.Model):

    post = models.ForeignKey('Post')

    user = models.ForeignKey(
            User,
            blank=True,
            null=True,
    )

    content = models.TextField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse(
                'posts:detail',
                kwargs={
                    'pk': self.post.id,
                },
        ) + '#comment-' + str(self.id)
