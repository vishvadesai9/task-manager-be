from rest_framework import viewsets
from rest_framework.response import Response

from apis.models import User, Tasks
from apis.serializers import UserSerializer
from passlib.hash import sha256_crypt

class SignUpView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = None
    queryset = User.objects.all()
    
    def create(self, request, *args, **kwargs):
        username = request.data["username"]
        username = username.strip()
        username_exists = self.queryset.filter(username=username).first()
        if username_exists:
            return Response({"success":False, "message": "username already exists"})
        else:
            request.data["password"] = sha256_crypt.encrypt(request.data["password"])
            return super().create(request, *args, **kwargs)