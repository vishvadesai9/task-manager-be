from rest_framework import viewsets
from rest_framework.response import Response
from dateutil.parser import parse

from apis.models import User, Tasks
from apis.serializers import TaskSerializer

class TasksView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    pagination_class = None
    queryset = Tasks.objects.all()

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get("user_id", "")
        user_id = user_id.strip()
        user_tasks = self.queryset.filter(user_id=user_id).order_by("-due_date")
        data = TaskSerializer(user_tasks, many=True).data
        return Response({"success": True, "data": data})

    def create(self, request, *args, **kwargs):
        request.data["due_date"] = parse(request.data["due_date"])
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        request.data["due_date"] = parse(request.data["due_date"])
        return super().update(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

