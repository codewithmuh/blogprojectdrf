from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# The RegisterSerializer class inherits from the Serializer class, and it has four fields: first_name,
# last_name, username, and password


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
    
class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already in use")
        
        return data
    

    def create(self, validated_data):
        user = User.objects.create(first_name= validated_data['first_name'],
           last_name= validated_data['last_name'],
           username = validated_data['username'].lower()
         )   
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

# The LoginSerializer class is a subclass of the Serializer class. It has two fields, username and
# password. The validate method checks if the username exists in the database. If it does not exist,
# it raises a validation error. The get_jwt_token method authenticates the user and returns a JWT
# token

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

            if not User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("Username does not Exist")

            return data


    def get_jwt_token(self, data):
    
        user = authenticate(username=data['username'], password= data['password'])
    
        if not user :
            return { 'message': "invalid Crendentials", 'data': {}}
    
        refresh = RefreshToken.for_user(user)
    
        return  { 'message': "Login Success", 'data': {'token': {  'refresh': str(refresh),
        'access': str(refresh.access_token),}}}
    
    