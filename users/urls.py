from django.urls import path
from rest_framework import routers

from users.views.paymant import PaymentListAPIView
from users.views.users import UserViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view()),
] + router.urls