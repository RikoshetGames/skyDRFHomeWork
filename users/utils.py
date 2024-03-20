import json
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def set_schedule(*args, **kwargs):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.DAYS
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name="Checking users",
        task="users.tasks.check_all_users_last_login",
        kwargs=json.dumps({
            "be_careful": True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )