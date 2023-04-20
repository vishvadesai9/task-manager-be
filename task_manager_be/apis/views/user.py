from rest_framework import viewsets
from rest_framework.response import Response

from apis.models import User, Tasks
from apis.serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = None
    queryset = User.objects.all()
    
    def create(self, request, *args, **kwargs):
        username = request.data["username"]
        username = username.strip()
        username_exists = self.queryset.filter(username=username).first()
        if username_exists:
            username_exists = UserSerializer(username_exists).data
            return Response({"success":True, "message": "Logged In", "userdata": username_exists})
        else:
            return super().create(request, *args, **kwargs)