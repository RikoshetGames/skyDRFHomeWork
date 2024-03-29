from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from tracker.models import Course, Lesson, Subscription
from users.models import User


class TrackerTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="user_test@mail.ru",
        )
        self.course = Course.objects.create(
            name="Course_1",
            description="CourseDescription_1",
            user=self.user
        )
        self.lesson = Lesson.objects.create(
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
            reverse('lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # print(response.json())

        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.lesson.id,
                        'name': self.lesson.name,
                        'preview': self.lesson.preview,
                        'description': self.lesson.description,
                        'video_link': self.lesson.video_link,
                        'course': self.lesson.course.id,
                        'user': self.lesson.user.id
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {
            "name": "Lesson_2",
            # "preview": "placeholder_preview.png",
            "description": "LessonDescription_2",
            "video_link": "https://www.youtube.com/watch?v=yourvideoid",
            "course": self.course.id,
            "user": self.lesson.user.id
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            reverse('lesson_create'),
            data=data
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
        # print(response.json())

    def test_update_lesson(self):
        """Тестирование обновления урока"""

        updated_data = {
            "name": "Updated Lesson Name",
            "description": "Updated Lesson Description",
            "video_link": "https://www.youtube.com/watch?v=yourvideoid",
            "course": self.course.id,
            "user": self.lesson.user.id
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.put(
            reverse('lesson_update', kwargs={'pk': self.lesson.id}),
            data=updated_data
        )

        # print(response.content)

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse('lesson_delete', kwargs={'pk': self.lesson.id}),
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_subscription_flag_for_retrieving_on_not_subscribed_user(self):
        Subscription.objects.all().delete()
        url = reverse('course-detail', kwargs={'pk': self.course.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.json()['is_subscribed'])

    def test_subscription_flag_for_retrieving_on_subscribed_user(self):
        Subscription.objects.create(course=self.course, user=self.user)
        url = reverse('course-detail', kwargs={'pk': self.course.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()['is_subscribed'])

class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="user_test@mail.ru"
        )
        self.course = Course.objects.create(
            name="Course_1",
            description="CourseDescription_1"
        )


    def test_subscribe_to_course(self):
        """Тестирование подписки на курс"""

        data = {
            "course": self.course.id,
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            reverse('subscription', kwargs={'pk': self.course.id}),
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

    def test_unsubscribe_from_course(self):
        """Тестирование отписки от курса"""

        subscription = Subscription.objects.create(
            course=self.course,
            user=self.user,
        )

        subscription.refresh_from_db()

        data = {
            "course": self.course.id,
        }

        self.client.force_authenticate(user=self.user)

        response_subscribe = self.client.post(
            reverse('subscription', kwargs={'pk': subscription.id}),
            data=data
        )

        self.assertEquals(
            response_subscribe.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response_subscribe.json(),
            {'message': 'Вы отписались от обновления курса'}
        )

        self.user.refresh_from_db()  # Обновляем данные пользователя из базы
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_subscribe_to_course_unauthorized(self):
        """Тестирование подписки на курс для неавторизованного пользователя"""

        data = {
            "course": self.course.id,
        }

        response = self.client.post(
            reverse('subscription', kwargs={'pk': self.course.id}),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertEquals(
            response.json(),
            {'detail': 'Учетные данные не были предоставлены.'}
        )

    def test_subscribe_to_not_existing_course(self):
        """Тестирование подписки на несуществующий курс"""

        not_existing_course = 8998

        data = {
            "course": not_existing_course,
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            reverse('subscription', kwargs={'pk': not_existing_course}),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        self.assertEquals(
            response.json(),
            {'detail': 'Страница не найдена.'}
        )


