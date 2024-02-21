from rest_framework import generics, filters
from users.models import Payment
from users.serializers.paymant import PaymentSerializer


class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['payment_date']
    search_fields = ['course_title', 'lesson_title', 'payment_method']