from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    """Allow read-only access to everyone."""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class ReadOnlyOrAdmin(permissions.BasePermission):
    """Read for everyone, write for admin only."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsOwnerOrAdmin(permissions.BasePermission):
    """Only the owner or an admin can access/modify."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user or request.user.is_staff
        return obj.user == request.user or request.user.is_staff
