from django.db import models

class User(models.Model):
        YEAR_1="Y_1"
        YEAR_2="Y_2"
        YEAR_3="Y_3"
        YEAR_4="Y_4"
        YEAR_OF_STUDY_CHOICES={
            Y_1:"year_1",
            Y_2:"year_2",  
            Y_3:"year_3",
            Y_4:"year_4",
        }
        
    
        fist_name=models.CharField(max_length=20) 
        last_name=models.CharField(max_length=20)
        year_of_study=models.CharField(max_length=3,choices=YEAR_OF_STUDY_CHOICES,default=y_1)

class Challenges(models.Model):
    challenge_name=models.charField(max_length=30)
    date_creation=models.DateTimeField(auto_now=True)
    replay=models.charField(max_length=500)
    comment=models.charField(max_length=500)
    likes=models.ManyToManyField(User)

    class User_profile(models.Model):
        user_id=models.BigIntegerField(max_length=16)
        Bio=models.charField(max_length=100)
        photo = models.ImageField(upload_to="default.jpj")
        class intake (models.Model):
            intake_id=models.BigIntegerField()