# Generated by Django 4.2.16 on 2024-11-30 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_bookmarkchallengecontainer_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmarkchallengecontainer',
            name='bookmark_name',
        ),
    ]