from django.urls import path
from rest_framework import routers

from tracker.views.course import CourseViewSet
from tracker.views.lesson import LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, LessonDestroyView
from tracker.views.subscription import SubscribeAPIView

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson_delete'),
    path('subscription/', SubscribeAPIView.as_view(), name='subscription'),
]


router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns += router.urls
