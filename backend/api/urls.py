from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path("hello/", views.hello_api, name="hello_api"),
    path("", include(router.urls)),
]
