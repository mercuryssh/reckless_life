from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=99)
    description = models.CharField(max_length=125)

    def __str__(selft):
        return selft.description


class Article(models.Model):
    title = models.CharField(max_length=99)
    description = models.CharField(max_length=255)
    url_name = models.CharField(max_length=99, unique=True)
    cover_url = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    autor_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tag_id.title} - {self.article_id.title}"
