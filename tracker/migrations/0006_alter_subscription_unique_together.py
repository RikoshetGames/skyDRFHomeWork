# Generated by Django 5.0.2 on 2024-03-10 06:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_alter_subscription_course_alter_subscription_status_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('user', 'course')},
        ),
    ]
