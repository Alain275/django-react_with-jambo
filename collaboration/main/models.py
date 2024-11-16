from django.db import models

class User(models.Model):
        YEAR_1="Y_1"
        YEAR_2="Y_2"
        YEAR_3="Y_3"
        YEAR_4="Y_4"
        YEAR_OF_STUDY_CHOICES={
             YEAR_1:"year_1",
             YEAR_2:"year_2",  
             YEAR_3:"year_3",
             YEAR_4:"year_4",
        }
        
    
        fist_name=models.CharField(max_length=20) 
        last_name=models.CharField(max_length=20)
        year_of_study=models.CharField(max_length=3,choices=YEAR_OF_STUDY_CHOICES,default=YEAR_1)

