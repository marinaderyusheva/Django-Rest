from rest_framework import permissions


# просматривать может любой пользователь, удалять только админ
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # если метод безопасный
        # предоставлены ли права доступа
        if request.method in permissions.SAFE_METHODS:
            return True
        # пользователь вошел как админ
        return bool(request.user and request.user.is_staff)


# изменять записи может только создатель
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user