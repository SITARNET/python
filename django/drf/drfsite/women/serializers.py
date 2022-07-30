from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id') # поля которые будут отправляться пользователю

