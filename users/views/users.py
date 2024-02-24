from rest_framework import viewsets

from users.models import User
from users.serializers.users import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer