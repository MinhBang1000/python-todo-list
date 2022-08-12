from django.urls import path, include
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TaskViewSet, basename="tasks")

urlpatterns = [
    path('',include(router.urls))
]