from .models import Project, Task, ActivityLog


class ProjectService:
    @staticmethod
    def create_project(name, description, owner):
        project = Project(name=name, description=description, owner=owner)
        project.save()
        ActivityLog.objects.create(user=owner, project=project, action="Created project")
        return project

    @staticmethod
    def add_member(project, user):
        project.members.add(user)
        project.save()
        ActivityLog.objects.create(user=user, project=project, action="Added member to project")

    @staticmethod
    def remove_member(project, user):
        project.members.remove(user)
        project.save()
        ActivityLog.objects.create(user=user, project=project, action="Removed member from project")


class TaskService:
    @staticmethod
    def create_task(title, description, project, due_date, assigned_to=None):
        task = Task(title=title, description=description, project=project, due_date=due_date, assigned_to=assigned_to)
        task.save()
        ActivityLog.objects.create(user=assigned_to or project.owner, task=task, action="Created task")
        return task

    @staticmethod
    def update_task_status(task, status):
        task.status = status
        task.save()
        ActivityLog.objects.create(user=task.assigned_to, task=task, action=f"Updated task status to {status}")

    @staticmethod
    def assign_task(task, user):
        task.assigned_to = user
        task.save()
        ActivityLog.objects.create(user=user, task=task, action="Assigned task")
