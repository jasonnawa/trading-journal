from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from journal.models import JournalEntry
from journal.views.analytics.calculations import calculate_summary


class AnalyticsViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def summary(self, request):
        trades = JournalEntry.objects.filter(user=request.user, exit_price__isnull=False)
        data = calculate_summary(trades)
        return Response(data)
