from rest_framework import fields, serializers
from . import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class ArticlePreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('title', 'description', 'url_name', 'date','tags')


class ProjectBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectPost
        fields = "__all__"
