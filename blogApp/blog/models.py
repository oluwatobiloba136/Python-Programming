from django.db import models
from django.utils  import timezone
from django.conf import settings
# Create your models here.

# This is our custom manager to retrieve all posts that have a PUBLISHED status
class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    # SUBCLASS for enum
    class Status(models.TextChoices):
        DRAFT ='DF','Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created =  models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    # The default manager for every model is the objects manager
    objects = models.Manager() # the default manager: This manager retrieves all the objects  in the database
    published = PublishedManager() # our custom manager

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title