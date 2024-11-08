from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project, Task
from .services import ProjectService, TaskService

User = get_user_model()


class ProjectServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")

    def test_create_project(self):
        project = ProjectService.create_project("New Project", "Description", self.user)
        self.assertEqual(project.name, "New Project")
        self.assertEqual(project.owner, self.user)


class TaskServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.project = Project.objects.create(name="Test Project", description="Description", owner=self.user)

    def test_create_task(self):
        task = TaskService.create_task("New Task", "Description", self.project, "2024-12-01", self.user)
        self.assertEqual(task.title, "New Task")
        self.assertEqual(task.project, self.project)
