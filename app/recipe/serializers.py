"""
Serializers for Recipe APIs.
"""
from rest_framework import serializers

from core.models import (
    Recipe,
    Tag,
)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects."""

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes', 'price', 'description')
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Create and return a new recipe."""
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing recipe."""
        instance.title = validated_data.get('title', instance.title)
        instance.time_minutes = validated_data.get('time_minutes', instance.time_minutes)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ('description',)


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create and return a new tag."""
        return Recipe.tags.through.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing tag."""
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
