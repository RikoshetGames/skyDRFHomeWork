from rest_framework import serializers, fields

from tracker.models import Course


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = fields.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lesson_count']

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()