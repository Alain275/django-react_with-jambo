from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True, default='')
    email = models.EmailField(unique=True,default='example@gmail.com')
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
         return self.full_name
    class Meta:
         ordering=['first_name']


class Student(models.Model):
     YEAR_1 = "Y_1"
     YEAR_2 = "Y_2"
     YEAR_3 = "Y_3"
     YEAR_4 = "Y_4"
    
     YEAR_OF_STUDY_CHOICES = [
        (YEAR_1, "Year 1"),
        (YEAR_2, "Year 2"),
        (YEAR_3, "Year 3"),
        (YEAR_4, "Year 4"),
     ]
   
     user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
     year_of_study = models.CharField(
        max_length=6,
        choices=YEAR_OF_STUDY_CHOICES,
        default=YEAR_1
     )
     Bio=models.CharField(max_length=100,null=True,blank=True)
     photo = models.ImageField(upload_to="default.jpj",null=True,blank=True)
    
     @property
     def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

     def __str__(self):
         return self.full_name

     def username(self):
        return self.user.username    
     def first_name(self):
        return self.user.first_name    
     def last_name(self):
        return self.user.last_name    
     class Meta:
         ordering=['user__first_name']
         permissions = [
             ('view_history','Can view history')
         ]


class intake (models.Model):
     intake_id=models.BigIntegerField(primary_key=True)
     user=models.ForeignKey(User,on_delete=models.CASCADE)

     def user_first_name(self, obj):
        return obj.user.first_name  # Assuming 'user' is the related field pointing to the User model
     user_first_name.short_description = 'User First Name'

     

     @staticmethod
     def ordinal(value):
        """
        Convert an integer to its ordinal string representation.
        """
        if 11 <= value % 100 <= 13:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(value % 10, "th")
        return f"{value}{suffix}"
     def __str__(self):
        return f"intake: {self.ordinal(self.intake_id)}"


     class Meta:
        ordering = ['intake_id']         
