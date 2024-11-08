from rest_framework import serializers
from .models import Project, Task, ActivityLog
from datetime import date


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Project name cannot be empty.")
        return data


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        if 'due_date' in data and data['due_date'] < date.today():
            raise serializers.ValidationError("The due date cannot be in the past.")
        return data


class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'
