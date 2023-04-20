from rest_framework import viewsets
from rest_framework.response import Response
from passlib.hash import sha256_crypt

from apis.models import User
from apis.serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = None
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        username = request.data["username"]
        username = username.strip()
        user_exists = self.queryset.filter(username=username).first()
        if user_exists:
            correct_password  = sha256_crypt.verify(request.data["password"], user_exists.password)
            if correct_password:
                user_data = UserSerializer(user_exists).data
                return Response({"success":True, "message": "Logged In", "userdata": user_data})
            else: 
                return Response({"success":False, "message": "Incorrect password"})

        else:
            return Response({"success":False, "message": "User does not exist"})