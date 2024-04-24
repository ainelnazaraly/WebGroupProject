from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, RecipeSerializer

from rest_framework.response import Response 
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime

class RegisterView(APIView): 
    def post(self, request): 
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView): 
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()
        
        if user is None: 
            raise AuthenticationFailed('User not found!')

        
        if not user.check_password(password): 
            raise AuthenticationFailed('Incorrect password')

        payload ={ 
            'id': user.id, 
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60), 
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value = token, httponly = True)
        response.data = { 
            'jwt': token
        }

        return response

class UserView(APIView): 
    def get(self, request): 
        token = request.COOKIES.get('jwt')

        if not token: 
            raise AuthenticationFailed('Unauthenticated')

        try: 
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: 
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView): 
    def post(self, request): 
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Review, Recipe
from .serializers import ReviewSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure user is authenticated
def create_review(request):
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            recipe_id = request.data.get('recipe_id')
            try:
                recipe = Recipe.objects.get(pk=recipe_id)
            except Recipe.DoesNotExist:
                return Response({'error': 'Recipe does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            serializer.save(user=request.user, recipe=recipe)  # Associate review with authenticated user and recipe
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_recipe(request):
    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  # Assign the current user as the author of the recipe
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def recipe_crud_user(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        return Response({'error': 'Recipe does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    if recipe.author != request.user:
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recipe.delete()
        return Response({'message': 'Recipe deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
# Create your views here.
