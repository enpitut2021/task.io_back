from rest_framework import routers
from .views import Daily_TaskViewSet
from .views import UserViewSet, TaskViewSet,ProgressViewSet
from django.urls import path

router = routers.SimpleRouter()

router.register(r"users", UserViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"daily_tasks",Daily_TaskViewSet)
router.register(r"progress",ProgressViewSet)



