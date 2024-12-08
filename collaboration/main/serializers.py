from . import models
from uuid import UUID
from django.db import transaction
from rest_framework import serializers
from .signals import order_created 

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Challenges
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__' 

class SimpleChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Challenges
        fields = ['challenge_name','date_creation','user','likes']       

class BookmarkChallengeItemSerializer(serializers.ModelSerializer):
    challenge = SimpleChallengeSerializer()
    class Meta:
        model = models.BookmarkChallengeItem
        fields = ['id','challenge','description','updated_at','created_at']  # Adjust fields if necessary

class BookmarkChallengeContainerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    bookmark_challenge_items = BookmarkChallengeItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.BookmarkChallengeContainer
        fields = ['id', 'user', 'created_at', 'bookmark_challenge_items']

class AddBookmarkChallengeItemSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = models.BookmarkChallengeItem
        fields = ['id','challenge','description']       
class UpdateBookmarkChallengeItemSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = models.BookmarkChallengeItem
        fields = ['description']  

class  OrderingFeedBackItemSerializer(serializers.ModelSerializer):
    challenge = SimpleChallengeSerializer()
    class Meta:
        model = models.OrderingFeedBackItem
        fields = '__all__'        

class OrderingFeedBackSerializer(serializers.ModelSerializer):
    odering_feedback_items = OrderingFeedBackItemSerializer(many=True,read_only=True)
    class Meta:
        model = models.OrderingFeedBack
        fields = ['ordered_at','payment_status','student','odering_feedback_items'] 
class UpdateOrderingFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderingFeedBack
        fields = ['payment_status'] 

class CreateOrderingFeedBackSerializer(serializers.Serializer):
    container_id = serializers.UUIDField()

    def save(self,**kwargs):
        with transaction.atomic():
            validated_data = self.validated_data
            container_id = validated_data['container_id']
            # print(self,validated_data['container_id'])  
            # print(self.context['user_id']) 

            student = models.Student.objects\
                    .get(user=self.context['user_id']) 
            odering=models.OrderingFeedBack.objects.create(student=student) 
            
            bookmark_challenge_container_items = models\
                    .BookmarkChallengeItem.objects\
                    .select_related('challenge')\
                    .filter(container_id=self.validated_data['container_id'])
            
            ordering_feedback_items=[
                    models.OrderingFeedBackItem(
                        odering=odering,
                        challenge=item.challenge,
                        description=item.description

                    )for item in bookmark_challenge_container_items
                ]
            models.OrderingFeedBackItem.objects.bulk_create(ordering_feedback_items)
            models.BookmarkChallengeContainer.objects.filter(pk=container_id).delete()

            order_created.send_robust(self.__class__,odering=odering)

            return odering
        
   

           

            


            
          

