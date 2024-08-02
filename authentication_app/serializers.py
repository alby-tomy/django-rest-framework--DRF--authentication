from rest_framework import serializers
from django.contrib.auth.models import User

# Create your models here.
class  RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self,data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError("Username already exists")
        
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError("Email is already taken")
            
        special_char = "!@#$%^&*()"
        if not any(c in special_char for c in data['password']):
            raise serializers.ValidationError(f"Password should contain atleast a special character {special_char}")
        
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
