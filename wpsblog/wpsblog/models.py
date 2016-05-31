from django.db import models


class Post(models.Model):
    title = models.CharField(
            max_length=120,
    )
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return '/posts/' + str(self.id) + '/'
