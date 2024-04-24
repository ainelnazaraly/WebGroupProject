from rest_framework import serializers
from .models import Category, Recipe, Review, NutritionInfo, User

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


# class RecipeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return Recipe.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.category_id = validated_data.get('category_id', instance.category_id)
#         instance.author_id = validated_data.get('author_id', instance.author_id)
#         instance.save()
#         return instance



class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'category', 'author', 'created_at', 'updated_at']


# Serializer using serializer.ModelSerializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'recipe', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['created_at']

# Serializer using serializer.ModelSerializer for NutritionInfo
class NutritionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionInfo
        fields = ['id', 'recipe', 'calories', 'fat', 'carbohydrates', 'protein']

class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = { 
            'password': {'write_only': True}
        }
    
    def create(self, validated_data): 
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance