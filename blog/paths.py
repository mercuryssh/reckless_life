from blog.models import Article
from django.urls import path
from .views import *

urlpatterns = [
    path('', say_hello),
    path('articles', ArticlesView.as_view(), name='Articles'),
    path('articles/<str:name>', ArticlesView.as_view(), name="article by name")
]
