from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, generics
from materials.models import Course
from materials.serializers import CourseSerializer, CourseDitailSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDitailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()
