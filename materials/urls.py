from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonDestroyApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView, SubscriptionViewSet,
    # SubscriptionViewSet,
)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register("course", CourseViewSet, basename="course")
router.register("subscription", SubscriptionViewSet, basename="subscription")

urlpatterns = [
    # lessons urls pattern
    path("lessons/", LessonListApiView.as_view(), name="list_lessons"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="create_lesson"),
    path("lessons/detail/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_detail",),
    path("lessons/update/<int:pk>/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path("lessons/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="lesson_delete"),
] + router.urls
