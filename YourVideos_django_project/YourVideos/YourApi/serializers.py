from rest_framework import serializers
from .models import Video, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class OurVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'category', 'auther', 'comments_list')
        extra_kwargs = {'url':{'required':True}}



class OurRatingSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'comments', 'video')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ('id', 'username', 'password')
        extra_kwrgs = {'password':{'required':True, 'write_only':True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.all(user=user)
            return user