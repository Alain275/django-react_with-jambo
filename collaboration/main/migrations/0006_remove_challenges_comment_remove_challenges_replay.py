# Generated by Django 4.2.16 on 2024-11-29 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_challenges_likes_alter_challenges_replay_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenges',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='challenges',
            name='replay',
        ),
    ]