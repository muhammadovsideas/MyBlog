from rest_framework import permissions

class IsAdminIsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.role in ["ADMIN", "USER"]:
            return True
        return False