from rest_framework.serializers import ModelSerializer
from django.apps import apps
NewsModel = apps.get_model('News', 'News')


class NewsSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['author', 'title', 'desc']
