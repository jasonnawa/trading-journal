from rest_framework import permissions

class CanEditOrReadOwnOrGlobalStrategy(permissions.BasePermission):
    """
    - Global strategies (owner=None) → read-only for everyone, write for admins only
    - User strategies (owner=user) → full access for that user, read-only for others
    """

    def has_object_permission(self, request, view, obj):
        # Everyone can read
        if request.method in permissions.SAFE_METHODS:
            return True

        # Global strategy → only admins can write
        if obj.owner is None:
            return request.user and request.user.is_staff

        # User strategy → owner or admin can write
        return obj.owner == request.user or request.user.is_staff
