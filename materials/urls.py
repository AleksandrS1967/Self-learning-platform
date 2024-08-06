from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")
router.register(r"lesson", LessonViewSet, basename="lesson")

urlpatterns = [
] + router.urls