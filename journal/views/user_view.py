from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from journal.serializers import UserSerializer
from journal.permissions import IsOwnerOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()  # admins see everyone
        return User.objects.filter(id=user.id) 
    
    def get_permissions(self):
        if self.action == 'create':
            return []
        # Admin-only can list all users
        if self.action == 'list':
            return [permissions.IsAdminUser()]
        return [perm() for perm in self.permission_classes]