from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail


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


class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("join-mailing-list", )

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        a = self.title
        b = self.message
        # emails = Subscribers.objects.all()
        email_list = list(Subscribers.objects.values_list("email", flat=True))
        # print(email_list)
        send_mail(str(a),
                  str(b),
                  'saadatpour.1993@gmail.com',
                  email_list,
                  fail_silently=False)
        super().save(*args, **kwargs)
