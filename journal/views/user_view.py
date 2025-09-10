from rest_framework import viewsets
from django.contrib.auth.models import User
from journal.serializers import UserSerializer
from journal.permissions import IsOwnerOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin]