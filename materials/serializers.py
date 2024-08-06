from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from materials.models import Course


class CourseSerializer(ModelSerializer):
    """Сериализатор курса."""
    class Meta:
        model = Course
        fields = "__all__"


class CourseDitailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'owner']