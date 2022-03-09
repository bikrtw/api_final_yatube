from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('pub_date',)
        optional_fields = ('group',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowField(serializers.Field):
    def to_internal_value(self, data):
        user = get_object_or_404(User, username=data)
        return user

    def to_representation(self, value):
        return value.username


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(required=False, read_only=True)
    following = FollowField()

    class Meta:
        fields = ('user', 'following')
        model = Follow
