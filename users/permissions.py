from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "Вы не модератор"

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class IsOwner(BasePermission):
    message = "Вы не владелец"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return request.method in ('GET', 'PUT', 'PATCH', 'DELETE')
        return False