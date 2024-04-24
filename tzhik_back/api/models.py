from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class Category(models.Model): 
    name = models.CharField(max_length=100)
    class Meta: 
        verbose_name_plural = "Categories"
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self): 
        return self.name
    
    def to_json(self): 
        return{ 
            'id': self.id, 
            'name': self.name, 
            'description': self.description,
            'image_url': self.image.url if self.image else None,
        }


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_url': self.image.url if self.image else None,
            'category': self.category.name,
            'author': self.author.email,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.recipe.title} by {self.user.username}"

    def to_json(self):
        return {
            'id': self.id,
            'recipe_id': self.recipe.id,
            'recipe_title': self.recipe.title,
            'user_id': self.user.id,
            'user_username': self.user.username,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

class NutritionInfo(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, related_name='nutrition_info')
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    # Add other nutritional fields as needed

    def __str__(self):
        return f"Nutrition Info for {self.recipe.title}"

    def to_json(self): 
        return { 

        }

# Create your models here.
