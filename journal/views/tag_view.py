from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from journal.models import Tag
from journal.serializers import TagSerializer
from journal.permissions import CanEditOrReadOwnOrGlobalTags


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,CanEditOrReadOwnOrGlobalTags]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return Tag.objects.all()

        if user.is_authenticated:
            return Tag.objects.filter(owner__isnull=True) | Tag.objects.filter(owner=user)

        # Anonymous users → only global tags
        return Tag.objects.filter(owner__isnull=True)


    def perform_create(self, serializer):
        user = self.request.user
        if user.is_staff:
            # Admin-created tags are global
            serializer.save(owner=None)
        else:
            serializer.save(owner=user)