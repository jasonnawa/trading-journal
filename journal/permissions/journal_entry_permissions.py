from rest_framework import permissions

class CanEditOwnJournal(permissions.BasePermission):
    """Only allow editing own journal entries."""
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff
