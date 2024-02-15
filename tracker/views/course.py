from rest_framework import viewsets

from tracker.models import Course
from tracker.seriallizers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer