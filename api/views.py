from django_filters import rest_framework as filters 
from rest_framework import viewsets

from .models import User, Task ,Daily_Task
from .serializer import UserSerialzer, TaskSerializer, Daily_TaskSerializer
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
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = FilterTask

class Daily_TaskViewSet(viewsets.ModelViewSet):
    queryset = Daily_Task.objects.all()
    serializer_class = Daily_TaskSerializer