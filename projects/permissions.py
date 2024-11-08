from rest_framework.permissions import BasePermission


class IsProjectOwnerOrMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user in obj.members.all()


class IsTaskAssigneeOrProjectMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assigned_to == request.user or request.user in obj.project.members.all()
