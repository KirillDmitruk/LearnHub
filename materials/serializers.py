from rest_framework.serializers import ModelSerializer

from materials.models import Course


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
