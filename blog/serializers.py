from rest_framework import fields, serializers
from . import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'
