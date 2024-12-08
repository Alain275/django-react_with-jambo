from django.db import models
from user.models import Student
from django.conf import settings
from django.contrib import admin
from django.utils import timezone
from uuid import uuid4


class BookmarkChallengeContainer(models.Model):
    """
    Represents a container that groups bookmarked challenges for a user.
    """
    id = models.UUIDField(primary_key=True,default=uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookmark_containers")
    # bookmark_name = models.CharField(max_length=100, default="My Bookmark's challenge")  # Optional, for multiple containers
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} (Owner: {self.user.first_name})"         



class Challenges(models.Model):
    challenge_name=models.CharField(max_length=30)
    date_creation=models.DateTimeField(auto_now=True)
    # replay = models.TextField(blank=True, null=True)  # Reply by post owner (optional)
    # comment=models.CharField(max_length=500, null=True,blank=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='Challenge',default=1)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_challenges',blank=True)

    def __str__(self):
         return self.challenge_name
    class Meta:
         ordering=['challenge_name']

class BookmarkChallengeItem(models.Model):
    """
    Represents a bookmarked item linked to a container and a blog post.
    """
    container = models.ForeignKey(BookmarkChallengeContainer, on_delete=models.CASCADE, related_name="bookmark_challenge_items")
    challenge = models.ForeignKey(Challenges, on_delete=models.CASCADE, related_name="bookmarked_items")
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bookmark: {self.challenge.challenge_name} in {self.container.id}"         






class Review(models.Model):
    RATING_CHOICES = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
]

    Challenge = models.ForeignKey('Challenges', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    reply = models.TextField(blank=True, null=True)  # Reply by post owner (optional)
    parent_reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')  # For nested replies
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.rating} stars"
    

class OrderingFeedBack(models.Model):
    PAYIMENT_STATUS_PENDING = 'P'    
    PAYIMENT_STATUS_COMPLETE = 'C'    
    PAYIMENT_STATUS_FAILED = 'F'    
    PAYIMENT_STATUS_CHOICE = [
         (PAYIMENT_STATUS_PENDING , 'Panding'),    
         (PAYIMENT_STATUS_COMPLETE , 'Complete'),   
         (PAYIMENT_STATUS_FAILED ,'Failed') 

    ]  

    ordered_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYIMENT_STATUS_CHOICE,default=PAYIMENT_STATUS_PENDING)
    student = models.ForeignKey(Student,on_delete=models.PROTECT)

    class Meta:
        permissions = [
            ('canel_order','Can cancel order')
        ] 


class OrderingFeedBackItem(models.Model):
    """
    Represents a bookmarked item linked to a container and a blog post.
    """
    odering = models.ForeignKey(OrderingFeedBack, on_delete=models.CASCADE, related_name="odering_feedback_items")
    challenge = models.ForeignKey(Challenges, on_delete=models.CASCADE, related_name="ordered_items")
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"orders: {self.challenge.challenge_name} in {self.odering.id}"         








     
        
