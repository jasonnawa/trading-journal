from rest_framework import serializers
from journal.models import Strategy

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ['id', 'owner', 'title', 'description']
        read_only_fields = ['owner']
