from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from .permissions import IsProjectOwnerOrMember, IsTaskAssigneeOrProjectMember
from .models import ActivityLog
from .serializers import ActivityLogSerializer
from django.core.mail import send_mail
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectOwnerOrMember]

    def perform_create(self, serializer):
        project = serializer.save(owner=self.request.user)
        ActivityLog.objects.create(user=self.request.user, project=project, action="Created project")

        self.send_email_notification(project, "New project created")

    def perform_update(self, serializer):
        project = serializer.save()
        ActivityLog.objects.create(user=self.request.user, project=project, action="Updated project")

        self.send_email_notification(project, "Project updated")

    def perform_destroy(self, instance):
        ActivityLog.objects.create(user=self.request.user, project=instance, action="Deleted project")
        super().perform_destroy(instance)
        self.send_email_notification(instance, "Project deleted")

    def send_email_notification(self, project, subject):
        members = project.members.all()
        recipient_list = [member.email for member in members]
        send_mail(
            subject,
            f"Dear members, the project '{project.name}' has been updated.",
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskAssigneeOrProjectMember]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'due_date', 'assigned_to']
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        task = serializer.save()
        ActivityLog.objects.create(user=self.request.user, task=task, action="Created task")

        self.send_email_notification(task, "New task created")

    def perform_update(self, serializer):
        task = serializer.save()
        ActivityLog.objects.create(user=self.request.user, task=task, action="Updated task")

        self.send_email_notification(task, "Task updated")

    def perform_destroy(self, instance):
        ActivityLog.objects.create(user=self.request.user, project=instance, action="Deleted project")
        super().perform_destroy(instance)
        self.send_email_notification(instance, "Project deleted")

    def send_email_notification(self, task, subject):
        assignee = task.assigned_to
        recipient_list = [assignee.email] if assignee else []
        if recipient_list:
            send_mail(
                subject,
                f"Dear {assignee.username}, the task '{task.title}' has been updated.",
                settings.EMAIL_HOST_USER,
                recipient_list,
                fail_silently=False,
            )


class ActivityLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ActivityLog.objects.filter(user=self.request.user)
