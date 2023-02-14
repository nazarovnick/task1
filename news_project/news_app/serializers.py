from rest_framework import serializers
from news_app.models import news_model


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news_model
        fields = ('__all__')