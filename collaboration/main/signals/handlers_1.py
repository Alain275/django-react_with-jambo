
from django.db.models.signals import post_save
from django.conf import settings
from user.models import Student
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_student_for_new_user(sender,**kwargs):
    if kwargs['created']:
        Student.objects.create(user=kwargs['instance'])