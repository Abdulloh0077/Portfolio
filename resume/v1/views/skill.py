from rest_framework import viewsets
from resume.models import SkillModels
from ..serializers.skill import *
from rest_framework import permissions
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters
# from django.db.models import Q

class SkillViewSets(viewsets.ModelViewSet):
    queryset = SkillModels.objects.all()
    allowed_methods = ['GET',]
    http_method_names = ['get']
    serializer_class = SkillsSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = SkillModels.objects.all()
        search = self.request.GET.get("search", None)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = SkillModels.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
        
        # if search is not None:
        #     queryset = queryset.filter(Q(title__icontains=search) )
        
        # return queryset

