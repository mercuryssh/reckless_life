from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Blog Models

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
    tags = models.JSONField()

    def __str__(self):
        return self.title


class ProjectPost(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=90)
    cover_url = models.CharField(max_length=255)
    url_name = models.CharField(max_length=99, unique=True)
    tags = models.JSONField()

    def __str__(self):
        return f"{self.name}"
