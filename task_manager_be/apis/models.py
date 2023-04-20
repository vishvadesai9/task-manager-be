import uuid
from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100,unique=True, null=False, blank=False)
    password = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tasks(models.Model):
    STATUS_TYPES = [
        ("To do", "To do"),
        ("Completed", "Completed"),
        ("In Progress", "In Progress")
    ]
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE, blank=False, null=False
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    due_date = models.DateTimeField()
    status = models.CharField(
        max_length=50, choices=STATUS_TYPES, default = "To do"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)