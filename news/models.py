from django.db import models


class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    posted_datetime = models.DateTimeField()

    def __str__(self):
        return self.title
