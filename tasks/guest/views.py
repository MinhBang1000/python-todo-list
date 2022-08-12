from rest_framework import viewsets, filters

from ..models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["id"]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)