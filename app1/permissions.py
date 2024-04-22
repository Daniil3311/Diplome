from rest_framework.permissions import BasePermission


class IsBuyer(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.type == 'buyer'


class IsShop(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.type == 'shop'

#
# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.user.id == request.user.id