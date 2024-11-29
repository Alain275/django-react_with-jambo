from django.db import models
from django.contrib import admin


class User(models.Model):
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
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    year_of_study = models.CharField(
        max_length=6,
        choices=YEAR_OF_STUDY_CHOICES,
        default=YEAR_1
    )
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
         return self.full_name
    class Meta:
         ordering=['first_name']



class Challenges(models.Model):
    challenge_name=models.CharField(max_length=30)
    date_creation=models.DateTimeField(auto_now=True)
    # replay = models.TextField(blank=True, null=True)  # Reply by post owner (optional)
    # comment=models.CharField(max_length=500, null=True,blank=True)
    user=models.ManyToManyField(User,blank=True)
    likes=models.ManyToManyField(User,related_name='liked_challenges',blank=True)

    def __str__(self):
         return self.challenge_name
    class Meta:
         ordering=['challenge_name']



class Review(models.Model):
    RATING_CHOICES = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
]

    Challenge = models.ForeignKey('Challenges', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    reply = models.TextField(blank=True, null=True)  # Reply by post owner (optional)
    parent_reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')  # For nested replies
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.rating} stars"




class User_profile(models.Model):
     user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
     Bio=models.CharField(max_length=100,null=True,blank=True)
     photo = models.ImageField(upload_to="default.jpj",null=True,blank=True)
    
     @property
     def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

     def __str__(self):
         return self.full_name
     class Meta:
         ordering=['user__first_name']

     
        
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