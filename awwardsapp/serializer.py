
from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("profile_pic","bio","location","user","account_url")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("user","title","description","project_image","project_url","pub_date","technologies")
