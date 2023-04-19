from django.contrib.postgres import fields
from rest_framework import serializers
from .models import (
    User,
    Tasks,
)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "user_id",
            "username",
            "created_at",
        )

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = (
            "task_id",
            "user_id",
            "title",
            "description",
            "due_date",
            "status",
            "created_at",
            "updated_at",
        )

