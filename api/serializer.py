from rest_framework import serializers

from .models import Daily_Task, User, Task, Progress


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)

class ProgressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Progress
        fields = ("progress","date")

class TaskSerializer(serializers.ModelSerializer):
    progress = ProgressSerializer(many=True)
    class Meta:
        model = Task
        fields = ("title", "detail", "tasktime","deadline","created_at","progress")


class Daily_TaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True)
    class Meta:
        model = Daily_Task
        fields = ("date","task")
    

