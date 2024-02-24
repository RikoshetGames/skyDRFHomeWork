from django.core.management.base import BaseCommand

from tracker.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='ID пользователя')
        parser.add_argument('course_id', type=int, help='ID курса')
        parser.add_argument('lesson_id', type=int, help='ID урока')

    def handle(self, *args, **options):
        user_id = options['user_id']
        course_id = options['course_id']
        lesson_id = options['lesson_id']

        try:
            user = User.objects.get(id=user_id)
            course = Course.objects.get(id=course_id)
            lesson = Lesson.objects.get(id=lesson_id)
            amount = 50.00
            payment_method = 'cash'

            payment = Payment.objects.create(
                user=user,
                payment_date='2022-01-01',
                course=course,
                lesson=lesson,
                amount=amount,
                payment_method=payment_method
            )
            payment.save()
            print("Платеж успешно создан.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
