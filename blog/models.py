from django.db import models
from django.urls import reverse
from django.utils import timezone


class PlainText(models.Model):
    body = models.TextField()


class Post(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")


class News(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    picture = models.ImageField(null=True, blank=True, upload_to="images/")

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Meta:
    ordering = ['created']
    indexes = [
        models.Index(fields=['created']),
    ]
