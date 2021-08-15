from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

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
    autor_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    tag_id = ForeignKey(Tag, on_delete=CASCADE)
    article_id = ForeignKey(Article, on_delete=CASCADE)

    def __str__(self):
        return f"{self.tag_id.title} - {self.article_id.title}"
