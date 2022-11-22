from rest_framework import permissions


class AdminOrAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return bool(obj.author_id == request.user or request.user.is_staff)
