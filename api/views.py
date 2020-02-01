from django.shortcuts import render

from .serializer import NewsSerializer
from rest_framework.viewsets import ModelViewSet
from django.apps import apps
NewsModel = apps.get_model('News', 'News')
# Create your views here.


class NewsView(ModelViewSet):
    queryset = NewsModel.objects.all().order_by('id')[:5]
    serializer_class = NewsSerializer

