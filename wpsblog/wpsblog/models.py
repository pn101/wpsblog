from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(
            max_length=120,
    )
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse(
                'post-detail',
                kwargs={
                    'post_id': self.id
                }
        )
