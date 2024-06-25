from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class TestLessons(APITestCase):
    """Тестирование уроков"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@example.com")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Python", description="Основы Python")
        self.lesson = Lesson.objects.create(
            title_course=self.course,
            title_lesson="ООП",
            description="Концепции ООП",
            owner=self.user,
            video_url="https://www.youtube.com/watch",
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""
        url = reverse("materials:create_lesson")
        data = {
            "title_lesson": "ООП",
            "description": "Основы ООП",
            "title_course": self.lesson.title_course.id,
            "video_url": "https://www.youtube.com/watch",
        }

        response = self.client.post(url, data=data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(data.get("title_lesson"), "ООП")
        self.assertEqual(data.get("title_course"), self.lesson.title_course.id)
        self.assertEqual(data.get("video_url"), "https://www.youtube.com/watch")
        self.assertEqual(data.get("description"), "Основы ООП")

    def test_update_lesson(self):
        """Тестирование изменений урока"""
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            "title_lesson": "ООП",
            "description": "Концепции ООП",
            "title_course": self.lesson.title_course.id,
            "video_url": "https://www.youtube.com/watch",
        }
        response = self.client.put(url, data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title_lesson"), self.lesson.title_lesson)
        self.assertEqual(data.get("description"), "Концепции ООП")
        self.assertEqual(data.get("title_course"), self.lesson.title_course.id)
        self.assertEqual(data.get("owner"), self.lesson.owner.id)

    def test_list_lesson(self):
        """Тестирование списка уроков"""
        url = reverse("materials:list_lessons")
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.id,
                    "title_lesson": self.lesson.title_lesson,
                    "description": self.lesson.description,
                    "preview": None,
                    "video_url": self.lesson.video_url,
                    "title_course": self.lesson.title_course.id,
                    "owner": self.lesson.owner.id,
                },
            ],
        }
        response = self.client.get(url)

        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_retrieve_lesson(self):
        """Тестирование просмотра одного урока"""
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title_lesson"), self.lesson.title_lesson)
        self.assertEqual(data.get("description"), self.lesson.description)
        self.assertEqual(data.get("title_course"), self.lesson.title_course.id)
        self.assertEqual(data.get("owner"), self.lesson.owner.id)

    def test_delete_lesson(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        print(response)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    """Тестирование подписок"""

    def setUp(self):
        self.user = User.objects.create(email="admin1@localhost")
        self.course = Course.objects.create(title="Python", description="Основы Python")
        self.client.force_authenticate(user=self.user)
        self.url = reverse("materials:subscription_create")

    def test_subscription_activate(self):
        """Тестирование активации подписки"""
        data = {"user": self.user.id, "course": self.course.id}
        response = self.client.post(self.url, data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.all().count(), 1)
        self.assertEqual(
            Subscription.objects.filter(user=self.user, course=self.course).exists(),
            True,
        )
        self.assertEqual(response.json().get("message"), "подписка добавлена")

    def test_subscription_deactivate(self):
        """Тестирование деактивации подписки"""
        data = {"user": self.user.id, "course": self.course.id}
        response = self.client.post(self.url, data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.all().count(), 0)
        # self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), False)
        self.assertEqual(response.json().get("message"), "подписка удалена")
