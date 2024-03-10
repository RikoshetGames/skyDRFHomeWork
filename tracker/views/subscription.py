from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.models import Course, Subscription


class SubscribeAPIView(APIView):

    def post(self, *args, **kwargs):

        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item, created = Subscription.objects.get_or_create(user=user, course=course_item)

        if created:
            message = 'Вы подписались на обновления курса'
        else:
            subs_item.delete()
            message = 'Вы отписались от обновления курса'

        return Response({"message": message})