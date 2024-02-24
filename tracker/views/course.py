from rest_framework.viewsets import ModelViewSet

from tracker.models import Course
from tracker.seriallizers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
