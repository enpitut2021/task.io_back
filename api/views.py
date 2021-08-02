import django_filters
from rest_framework import viewsets, filters

from .models import User, Task
from .serializer import UserSerialzer, TaskSerializer
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
