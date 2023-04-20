from apis.views import UserView, TasksView, SignUpView
from rest_framework import routers
from django.urls import path


router = routers.SimpleRouter()
router.register(r"tasks", TasksView, basename="tasks")
router.register(r"login", UserView, basename="login")
router.register(r"signup", SignUpView, basename="signup")


urlpatterns =[
    ]

urlpatterns += router.urls