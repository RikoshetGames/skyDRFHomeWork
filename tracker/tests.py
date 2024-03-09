from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from tracker.models import Course, Lesson, Subscription
from users.models import User


class TrackerTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            email="user_test@mail.ru",
            phone="1357986420",
            city="Moscow",
        )
        self.course = Course.objects.create(
            id=2,
            name="Course_1",
            description="CourseDescription_1",
            user=self.user
        )
        self.lesson = Lesson.objects.create(
            id=3,
            name="Lesson_1",
            description="LessonDescription_1",
            video_link="test.youtube.com",
            course=self.course,
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_list_lessons(self):
        """Тестирование вывода списка уроков"""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('tracker:lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.lesson.id,
                        'title': self.lesson.title,
                        'preview': self.lesson.preview,
                        'description': self.lesson.description,
                        'video_link': self.lesson.video_link,
                        'course': self.lesson.course,
                        'owner': self.user.id
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {
            "name": "test_lesson2",
            "description": "test_lesson2",
            "course": 1
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            reverse('tracker:lesson_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_lesson(self):
        """Тестирование изменения информации об уроке"""
        lesson = Lesson.objects.create(
            name='Test_lesson',
            description='Test_lesson',
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            f'/tracker/update/{lesson.id}/',
            {'description': 'change'}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        lesson = Lesson.objects.create(
            name='Test_lesson',
            description='Test_lesson',
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/tracker/delete/{lesson.id}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            username="user_test",
            email="user_test@mail.ru",
            phone="1357986420",
            city="Moscow",
        )

        self.course = Course.objects.create(
            name="Course_1",
            description="CourseDescription_1",
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):

        data = {
            "user": self.user.id,
            "course": self.course.id,
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            reverse('tracker:subscription'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'message': 'Вы подписались на обновления курса'}
        )