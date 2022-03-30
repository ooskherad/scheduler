from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'permission Denied, fuck you'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
