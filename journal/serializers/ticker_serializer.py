from rest_framework import serializers
from journal.models import Ticker

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ['id', 'symbol', 'name']
