from django.db import models
from django.utils import timezone

class Module(models.Model):
    """Module, that accepts comments."""

    title = models.CharField('title', max_length=200)
    # slug = models.SlugField('slug', unique_for_date='publish')
    body = models.TextField('body')
    allow_comments = models.BooleanField('allow comments', default=True)
    publish = models.DateTimeField('publish', default=timezone.now)