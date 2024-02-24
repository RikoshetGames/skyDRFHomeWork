from django.db import models
from django.contrib.auth.models import AbstractUser

from tracker.models import Course, Lesson

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('transfer', 'Transfer')], verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return self.user
