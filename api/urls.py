from rest_framework import routers
from .views import Daily_TaskViewSet, UserViewSet, TaskViewSet


router = routers.SimpleRouter()

router.register(r"users", UserViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"daily_tasks",Daily_TaskViewSet)
