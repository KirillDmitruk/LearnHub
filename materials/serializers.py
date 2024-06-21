from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.validators import YouTubeValidation


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YouTubeValidation(field='video_url')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons_list = LessonSerializer(source='lessons', many=True, read_only=True)

    @staticmethod
    def get_lessons_count(obj):
        return Lesson.objects.filter(title_course=obj).count()  # Фильтр (указываем по какому полю будет идти подсчет)

    class Meta:
        model = Course
        fields = ("id", "title", "description", "lessons_count", "lessons_list")
