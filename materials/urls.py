from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateApiView,
                             LessonDestroyApiView, LessonListApiView,
                             LessonRetrieveApiView, LessonUpdateApiView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="list_lessons"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="create_lesson"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lessons/create/<int:pk>/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path("lessons/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="lesson_delete"),
]

urlpatterns += router.urls
