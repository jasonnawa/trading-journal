from rest_framework import permissions

class CanEditOrReadOwnOrGlobalTags(permissions.BasePermission):
    """
    - Global tags (owner=None) → read-only for everyone, write for admins only
    - User tags (owner=user) → full access for that user, read-only for others
    """

    def has_object_permission(self, request, view, obj):
        # Everyone can read
        if request.method in permissions.SAFE_METHODS:
            return True

        # Global tag → only admins can write
        if obj.owner is None:
            return request.user and request.user.is_staff

        # User tag → owner or admin can write
        return obj.owner == request.user or request.user.is_staff
