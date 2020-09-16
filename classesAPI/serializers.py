from rest_framework import serializers
from django.contrib.auth.models import User

class RigesterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User 
        fields = ['username', 'password', 'first_name', 'last_name',]
    
    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.set_password(new_user.password)
        new_user.save()
        return validated_data

