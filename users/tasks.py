from celery import shared_task
from users.models import User
from datetime import datetime, timedelta


@shared_task
def check_all_users_last_login():
    date_x = datetime.now() - timedelta(days=30)
    users = User.objects.all()
    for user in users:
        if user.last_login < date_x:
            user.is_active = False
            user.save()
            print(f"{user} был деактивирован")