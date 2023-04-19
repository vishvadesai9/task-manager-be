from rest_framework import viewsets
from rest_framework.response import Response

from apis.models import User, Tasks
from apis.serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = None
    queryset = User.objects.all()