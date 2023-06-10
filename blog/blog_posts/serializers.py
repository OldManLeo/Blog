from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'tags', 'owner', 'post_date', 'img', 'author']
        read_only_fields = ['post_date']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        owner_username = validated_data.pop('owner')
        owner = User.objects.get(username=owner_username)
        post = Post.objects.create(owner=owner, **validated_data)
        for tag in tags_data:
            post.tags.add(tag)
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        instance = super().update(instance, validated_data)
        instance.tags.set(tags_data)
        return instance


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']




