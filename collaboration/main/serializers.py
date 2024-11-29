from . import models
from rest_framework import serializers


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Challenges
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'      