from rest_api import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user


class IsOwner(permissions.BasePermission):
    """
    Handles permissions for users.  The basic rules are

     - owner may GET, PUT, POST, DELETE
     - nobody else can access
    """

    def has_object_permission(self, request, view, obj):
        # permissions are only allowed to the owner of the snippet.
        return obj.user == request.user


class ReadOnly(permissions.BasePermission):
    """
    Handles permissions for users.  The basic rules are

     - anyone can may GET,
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return False