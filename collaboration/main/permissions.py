from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.id and request.user.is_staff)
    
class ViewCustomerHistory(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('main.view_history')
