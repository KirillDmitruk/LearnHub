from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """ Проверяет, является ли пользователь модератором """

    message = "Adding customers not allowed."

    def has_permission(self, request, view):
        if request.user.groups.filter(name="moder").exists():
            return True
        return False


class IsOwner(permissions.BasePermission):
    """ Проверяет, является ли пользователь владельцем """

    message = "You must be the owner of this content."

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
