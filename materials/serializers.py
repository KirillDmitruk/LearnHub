from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import YouTubeValidation


class LessonSerializer(serializers.ModelSerializer):
    """ Сериализатор Урока """
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YouTubeValidation(field="video_url")]


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор Курса """

    lessons_count = SerializerMethodField()
    lessons_list = LessonSerializer(source="lessons", many=True, read_only=True)

    @staticmethod
    def get_lessons_count(obj):
        return Lesson.objects.filter(
            title_course=obj
        ).count()  # Фильтр (указываем по какому полю будет идти подсчет)

    class Meta:
        model = Course
        fields = ("id", "title", "description", "lessons_count", "lessons_list")


class SubscriptionSerializer(serializers.ModelSerializer):
    """ Сериализатор Подписки """

    class Meta:
        model = Subscription
        fields = "__all__"
