from rest_framework import serializers
from . models import Profile, Post

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','image','title','description',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','profile_picture','first_name','second_name', 'bio')

