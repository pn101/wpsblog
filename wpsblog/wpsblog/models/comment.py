from django.db import models
from django.core.urlresolvers import reverse


class Comment(models.Model):

    post = models.ForeignKey('Post')
    content = models.TextField()

    def __str__(self):
        return self.content
