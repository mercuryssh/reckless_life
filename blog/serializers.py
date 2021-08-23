from rest_framework import fields, serializers
from . import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class ArticleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('title', 'description', 'url_name', 'date')


class ProjectBlogSerializar(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectPost
        fields = '__all__'
