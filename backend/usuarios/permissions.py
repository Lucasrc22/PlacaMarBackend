from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permissão customizada:
    - Usuários admin podem fazer qualquer ação
    - Usuários normais apenas leitura
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permissão customizada:
    - O usuário pode acessar/editar seu próprio perfil
    - Admin pode acessar/editar qualquer perfil
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff
