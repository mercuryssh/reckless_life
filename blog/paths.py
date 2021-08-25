from blog.models import Article
from django.urls import path
from .views import *

urlpatterns = [
    path('', say_hello),
    path('articles', ArticlesView.as_view(), name='Articles view'),
    path('articles/<str:name>', ArticlesView.as_view(), name="article by name"),

    # Project blog
    path('projects', ProjectsBlogView.as_view(), name='Projects view'),
    path('projects/<str:name>', ProjectsBlogView.as_view(), name='Project bt name')
]
