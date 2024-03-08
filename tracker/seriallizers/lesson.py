from rest_framework import serializers

from tracker.models import Lesson
from tracker.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video_link')]