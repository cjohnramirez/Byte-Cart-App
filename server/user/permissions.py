from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    #SAFE_METHODS is a list of read-only methods (GET, HEAD, OPTIONS). If request.method is in this list, access is granted to all users.
    if request.method in permissions.SAFE_METHODS:
      return True
    
    #If the method isn't in `SAFE_METHODS`, the code grants access only if the user is the owner.
    return obj.owner == request.user