from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from journal.models import Strategy
from journal.serializers import StrategySerializer
from journal.permissions import CanEditOrReadOwnOrGlobalStrategy


class StrategyViewSet(viewsets.ModelViewSet):
    serializer_class = StrategySerializer
    permission_classes = [IsAuthenticatedOrReadOnly,CanEditOrReadOwnOrGlobalStrategy]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return Strategy.objects.all()

        if user.is_authenticated:
            return Strategy.objects.filter(owner__isnull=True) | Strategy.objects.filter(owner=user)

        # Anonymous users → only global strategies
        return Strategy.objects.filter(owner__isnull=True)


    def perform_create(self, serializer):
        user = self.request.user
        if user.is_staff:
            # Admin-created strategies are global
            serializer.save(owner=None)
        else:
            serializer.save(owner=user)