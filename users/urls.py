from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views.paymant import PaymentListAPIView
from users.views.users import UserListAPIView, UserCreateAPIView, UserDetailAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

app_name = 'users'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-get'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name='user-delete'),
    path('payment/', PaymentListAPIView.as_view()),
]
