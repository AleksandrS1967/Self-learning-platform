from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    LessonViewSet,
    TestViewSet,
    AttemptAnswerCreateAPIView,
)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet,
                basename="course")
router.register(r"lesson", LessonViewSet,
                basename="lesson")
router.register(r"test", TestViewSet,
                basename="test")

urlpatterns = [
    path("answer/create/", AttemptAnswerCreateAPIView.as_view(),
         name="answer_create"),
] + router.urls
