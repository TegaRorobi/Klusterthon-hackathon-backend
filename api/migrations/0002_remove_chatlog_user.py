# Generated by Django 4.2.2 on 2023-11-24 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatlog',
            name='user',
        ),
    ]
