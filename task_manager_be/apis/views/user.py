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
        duplicate = self.queryset.filter(username=username)
        print(duplicate)
        if duplicate:
            return Response({"success":False, "message": "This username already exists. Try another username."})
        else:
            return super().create(request, *args, **kwargs)