from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FddgfghfViewSet

router = DefaultRouter()
router.register("fddgfghf", FddgfghfViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
