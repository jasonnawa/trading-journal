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


from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    - For User objects: only allow the user themselves or an admin.
    - For other objects with `.user`: only allow the owner or an admin.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only methods: allow safe access for everyone
        if request.method in permissions.SAFE_METHODS:
            if isinstance(obj, request.user.__class__):  # If obj is a User
                return obj == request.user or request.user.is_staff
            return getattr(obj, "user", None) == request.user or request.user.is_staff

        # Write/update methods
        if isinstance(obj, request.user.__class__):  # User object
            return obj == request.user or request.user.is_staff
        return getattr(obj, "user", None) == request.user or request.user.is_staff

