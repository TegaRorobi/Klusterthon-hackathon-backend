# Generated by Django 4.2.2 on 2023-11-22 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_managers_user_chat_logs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2023, 11, 22, 18, 33, 33, 690286, tzinfo=datetime.timezone.utc), verbose_name='last login'),
            preserve_default=False,
        ),
    ]
