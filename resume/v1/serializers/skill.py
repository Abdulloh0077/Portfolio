from rest_framework import serializers
from resume.models import SkillModels

class SkillsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillModels
        fields = ['photo', 'title']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillModels
        fields = ['url']

