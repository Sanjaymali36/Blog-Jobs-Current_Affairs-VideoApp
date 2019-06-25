from rest_framework import serializers
from news.models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'news_text',
            'title',
            'category',
            'date',
            'source',
            'link1'
        ]

