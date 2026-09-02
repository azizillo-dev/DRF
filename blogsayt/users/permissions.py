from rest_framework.permissions import BasePermission
from posts.models import Post

class IsLoggedIn(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated



class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
