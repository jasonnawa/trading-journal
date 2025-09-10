from rest_framework import serializers
from journal.models import Tag


class TagSerializer(serializers.Serializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']