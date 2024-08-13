from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверяем, является ли пользователь модератором"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()


class IsTeacher(permissions.BasePermission):
    """Проверка, является ли пользователь учителем"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="teacher").exists()


class IsOwner(permissions.BasePermission):
    """Проверяем, является ли пользователь владельцем"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
