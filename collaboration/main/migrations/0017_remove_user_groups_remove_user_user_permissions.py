# Generated by Django 4.2.16 on 2024-12-03 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rename_user_profile_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
