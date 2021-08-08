from django_filters import rest_framework as filters 
from rest_framework import viewsets

from .models import User, Task, Daily_Task, Progress
from .serializer import UserSerialzer, TaskSerializer
from .serializer import Daily_TaskSerializer, ProgressSerializer
from rest_framework.decorators import action
import datetime
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer

class FilterTask(filters.FilterSet):
    day = filters.DateTimeFilter(field_name='deadline', lookup_expr='gte')

    class Meta:
        model = Task
        fields = []


class TaskViewSet(viewsets.ModelViewSet):
    tasks = Task.objects.all()
    for task in tasks:
        duration = task.deadline.date() - datetime.datetime.now().date()
        duration_days=duration.days
        if duration.days < 0:
            duration_days=0
        progress = 100/(duration_days+1)
        p = Progress.objects.create(date=datetime.datetime.now(), progress=progress, task=task)
        task.progress.add(p)
        task.save()
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = FilterTask


class Daily_TaskViewSet(viewsets.ModelViewSet):
    daily_tasks = Daily_Task.objects.all()
    
    for daily_task in daily_tasks:
        date_today = daily_task.date
        tasks_add = Task.objects.filter(deadline__gte=date_today)
        for task_add in tasks_add:
            daily_task.task.add(task_add)
        daily_task.save()
        #for each_progress in progress:
        #    if daily_task.date.date() == each_progress.date.date():
        #        task=daily_task.task
        #        task.progress.add(each_progress)
        #        daily_task.save()
    queryset = Daily_Task.objects.all()
    serializer_class = Daily_TaskSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    
    queryset = Progress.objects.all()

    serializer_class = ProgressSerializer

