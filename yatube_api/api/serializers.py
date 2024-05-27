# Thirdparty imports
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField

# Projects imports
from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    following = serializers.CharField(max_length=64)

    def create(self, validated_data):
        username = validated_data['following']
        following = get_object_or_404(User, username=username)
        validated_data['following'] = following
        return Follow.objects.create(**validated_data)

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user',)
            )
        ]


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
