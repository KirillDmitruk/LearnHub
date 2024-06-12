from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons_list = LessonSerializer(source="lessons", many=True)

    @staticmethod
    def get_lessons_count(obj):
        return Lesson.objects.filter(title_course=obj).count()

    class Meta:
        model = Course
        fields = ("title", "description", "lessons_count", "lessons_list")
