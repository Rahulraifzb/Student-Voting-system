from rest_framework import fields, serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=125)
    last_name = serializers.CharField(max_length=125)
    email = serializers.EmailField(max_length=150,min_length=4)
    password = serializers.CharField(max_length=65,min_length=6,write_only=True)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password"]

    def validate(self,attrs):
        username = attrs.get("username","")
        email = attrs.get("email","")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username":("Username is already in use")})

        elif User.objects.filter(email=email).exists():
                raise serializers.ValidationError({"email":("Email is already in use")})

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255,min_length=2)
    password = serializers.CharField(max_length=65,min_length=6,write_only=True)

    class Meta:
        model = User 
        fields = ["username","password"]