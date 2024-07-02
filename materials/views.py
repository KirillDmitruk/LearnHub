from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status

from materials.models import Course, Lesson, Subscription
from materials.paginators import MaterialsPagination
from materials.serializers import (
    CourseSerializer,
    LessonSerializer,
    SubscriptionSerializer,
)
from materials.tasks import send_mail_notification
from users.permisions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """Course view set"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = MaterialsPagination

    def get_permissions(self):  # Проверка прав группы модераторов для курсов (нельзя создавать и удалять курс).
        if self.action in ("create",):
            self.permission_classes = ~IsModerator
        elif self.action in ("update",):
            self.permission_classes = IsModerator | IsOwner
        elif self.action == "destroy":
            self.permission_classes = ~IsModerator | IsOwner
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        send_mail_notification.delay(course_id=instance.id)


class LessonCreateApiView(CreateAPIView):
    """Create a Lesson"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~IsModerator, IsAuthenticated]


class LessonListApiView(ListAPIView):
    """List of Lessons"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPagination


class LessonRetrieveApiView(RetrieveAPIView):
    """Retrieve a Lesson"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated | IsModerator | IsOwner]


class LessonUpdateApiView(UpdateAPIView):
    """Update a Lesson"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated | IsModerator | IsOwner]


class LessonDestroyApiView(DestroyAPIView):
    """Delete a Lesson"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]


class SubscriptionViewSet(viewsets.ModelViewSet):
    """Subscription view set"""

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)

        subscription, created = Subscription.objects.get_or_create(user=user, course=course_item)
        if not created:
            subscription.delete()
            message = 'Subscription removed'
        else:
            message = 'Subscription added'

        return Response({"message": message})
