from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='tracker/', verbose_name='Превью курса', **NULLABLE)
    description = models.TextField(verbose_name='Описание курса')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название урока', unique=True)
    preview = models.ImageField(upload_to='tracker/', verbose_name='Превью урока', **NULLABLE)
    description = models.TextField(verbose_name='Описание урока')
    video_link = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
