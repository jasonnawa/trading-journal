from rest_framework import serializers
from journal.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'owner']
        read_only_fields = ['owner']