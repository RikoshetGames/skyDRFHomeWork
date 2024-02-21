from django.urls import path
from rest_framework import routers

from tracker.views.course import CourseViewSet
from tracker.views.lesson import LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, LessonDestroyView

urlpatterns = [
    path('', LessonListView.as_view()),
    path('<int:pk>/', LessonDetailView.as_view()),
    path('create/', LessonCreateView.as_view()),
    path('update/<int:pk>/', LessonUpdateView.as_view()),
    path('delete/<int:pk>/', LessonDestroyView.as_view()),
]


router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns += router.urls

