from rest_framework import serializers

from .models import Daily_Task, User, Task

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "detail", "tasktime","deadline","created_at")

class Daily_TaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer
    class Meta:
        model = Daily_Task
        fields = ("date","task")
    