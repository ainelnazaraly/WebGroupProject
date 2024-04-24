
from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, create_review, add_recipe, recipe_crud_user
from .category_views import CategoriesCRUD, CategoryCRUD 
from .recipe_views import recipe_detail, recipe_list, recipes_by_category
from .review_view import review_by_recipe, review_detail, review_list
from .nutrition_info_views import NutritionInfoCRUD, NutritionInfosCRUD, NutritionInfoByRecipe


urlpatterns = [
    path('register', RegisterView.as_view()), 
    path('login',LoginView.as_view()), 
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

    path('categories/', CategoriesCRUD.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoryCRUD.as_view(), name='category-detail'),

    path('recipes/', recipe_list, name='recipe-list'),
    path('recipes/<int:id>/', recipe_detail, name='recipe-detail'),
    path('recipes/category/<int:category_id>/', recipes_by_category, name='recipes-by-category'), 

    path ('reviews/', review_list, name='review-list'),
    path('review/<int:id>/', review_detail, name='review-detail'), 
    path('reviews/recipe/<int:recipe_id>/', review_by_recipe, name='review-by-recipe'), 

    path('nutritions/', NutritionInfosCRUD.as_view()), 
    path('nutrition/<int:id>', NutritionInfoCRUD.as_view()), 
    path('nutritions/recipe/<int:recipe_id>/', NutritionInfoByRecipe.as_view() ),



    path('create-review/', create_review, name='create_review'),
    path('add-recipe/', add_recipe, name='add_recipe'),
    path('recipe-crud/<int:recipe_id>/', recipe_crud_user, name='recipe_crud_user'),
]