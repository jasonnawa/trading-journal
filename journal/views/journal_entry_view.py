from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from journal.models import JournalEntry
from journal.serializers import JournalEntrySerializer
from journal.permissions import CanEditOwnJournal


class JournalEntryView(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated, CanEditOwnJournal]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return JournalEntry.objects.all()
        return JournalEntry.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    