from . import models
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField( read_only=True)
    username = serializers.CharField()  # Allow input, but not part of response
    full_name = serializers.CharField()  # Allow input, but not part of response
    first_name = serializers.CharField()  # Allow first name to be updated
    last_name = serializers.CharField()  # Allow last name to be updated
    
    class Meta:
        model = models.Student
        fields = ['user','year_of_study','Bio','photo','username','full_name','first_name','last_name']

        
        

    def update(self, instance, validated_data):
        # Handle updating first_name and last_name
        username = validated_data.pop('username', None)
        first_name = validated_data.pop('first_name', None)
        last_name = validated_data.pop('last_name', None)
        
        if first_name:
            instance.user.first_name = first_name
        if last_name:
            instance.user.last_name = last_name
        
        # Save the changes to the user
        instance.user.save()
        
        # Update the student instance itself
        return super().update(instance, validated_data)