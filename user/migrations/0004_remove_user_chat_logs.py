# Generated by Django 4.2.2 on 2023-11-24 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_groups_remove_user_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='chat_logs',
        ),
    ]