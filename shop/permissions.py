from rest_framework import permissions


class BasePermission(permissions.BasePermission):
    error_key = None

    def is_update(self, request):
        return request.method in ('PUT', 'PATCH')

    def is_delete(self, request):
        return request.method == 'DELETE'

    def is_get(self, request):
        return request.method == 'GET'

    def is_create(self, request):
        return request.method == 'POST'


class CanCreateUpdateDestroyHat(BasePermission):

    def has_permission(self, request, view):
        if (
            self.is_create(request) or
            self.is_update(request) or
            self.is_delete(request)
        ):
            if not request.user.is_superuser:
                view.error_key = 'unauthorized'
                return False
        return True


class CanCreateUpdateDestroyFootwear(BasePermission):

    def has_permission(self, request, view):
        if (
            self.is_create(request) or
            self.is_update(request) or
            self.is_delete(request)
        ):
            if not request.user.is_superuser:
                view.error_key = 'unauthorized'
                return False
        return True


class CanCreateUpdateDestroyBrand(BasePermission):

    def has_permission(self, request, view):
        if (
            self.is_create(request) or
            self.is_update(request) or
            self.is_delete(request)
        ):
            if not request.user.is_superuser:
                view.error_key = 'unauthorized'
                return False
        return True
