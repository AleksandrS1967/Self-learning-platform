from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from materials.models import Course, Lesson, Test, AttemptAnswer


class CourseSerializer(ModelSerializer):
    """Сериализатор курса."""

    class Meta:
        model = Course
        fields = "__all__"


class CourseDitailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "description", "owner"]


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class AttemptAnswerSerializer(ModelSerializer):
    class Meta:
        model = AttemptAnswer
        fields = "__all__"
