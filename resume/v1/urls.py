from django.shortcuts import render
from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsAdminUserOrReadOnly, IsOwnerOrReadonly

router = routers.DefaultRouter()
router.register(r'skills', SkillViewSets, basename="skills")

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
