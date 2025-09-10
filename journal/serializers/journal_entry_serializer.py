from rest_framework import serializers
from journal.models import JournalEntry, Strategy, Tag, Ticker
from .strategy_serializer import StrategySerializer
from .ticker_serializer import TickerSerializer
from .tag_serializer import TagSerializer


class JournalEntrySerializer(serializers.ModelSerializer):
    # Read-only nested representations
    strategy = StrategySerializer(read_only=True)
    ticker = TickerSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    # Write-only ID fields for creation/update
    strategy_id = serializers.PrimaryKeyRelatedField(
        queryset=Strategy.objects.all(), source="strategy", write_only=True
    )
    ticker_id = serializers.PrimaryKeyRelatedField(
        queryset=Ticker.objects.all(), source="ticker", write_only=True
    )
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), source="tags", many=True, write_only=True
    )

    class Meta:
        model = JournalEntry
        fields = [
            'id',
            'user',
            'ticker',
            'strategy',
            'tags',
            'quantity',
            'entry_price',
            'exit_price',
            'trade_date',
            'notes',
        ]
