from rest_framework import permissions


class CustomerAccessPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moder').exists():
            return True
        return False
