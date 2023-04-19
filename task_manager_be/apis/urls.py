from apis.views import UserView, TasksView
from rest_framework import routers
from django.urls import path


router = routers.SimpleRouter()
router.register(r"tasks", TasksView, basename="tasks")
router.register(r"login", UserView, basename="login")

urlpatterns =[
    # path("eou/", TasksView.as_view(), name="eou"),
    ]

urlpatterns += router.urls