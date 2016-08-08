from django.db import models
from django.utils import timezone

class Page(models.Model):

    title = models.CharField(max_length=255, null=False, blank=True, unique=True)
    summary = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date_added = models.DateField(auto_created=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title


class Comments(models.Model):

    page = models.ForeignKey(Page)

    comment_author = models.CharField(max_length=150)
    comment_date = models.DateTimeField(default=timezone.now)
    comment_body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.comment_body
