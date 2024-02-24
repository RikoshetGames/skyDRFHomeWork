from rest_framework import serializers, fields

from tracker.models import Course
from tracker.seriallizers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = fields.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lesson_count', 'lessons']
