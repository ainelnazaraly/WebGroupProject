from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NutritionInfo
from .serializers import NutritionInfoSerializer

class NutritionInfosCRUD(APIView):
    def get(self, request):
        nutritionInfos = NutritionInfo.objects.all()
        serializer = NutritionInfoSerializer(nutritionInfos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NutritionInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NutritionInfoCRUD(APIView):
    def get_object(self, pk):
        try:
            return NutritionInfo.objects.get(pk=pk)
        except NutritionInfo.DoesNotExist:
            return None

    def get(self, request, pk):
        nutritionInfo = self.get_object(pk)
        if nutritionInfo:
            serializer = NutritionInfoSerializer(nutritionInfo)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        nutritionInfo = self.get_object(pk)
        if nutritionInfo:
            serializer = NutritionInfoSerializer(nutritionInfo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        nutritionInfo = self.get_object(pk)
        if nutritionInfo:
            nutritionInfo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class NutritionInfoByRecipe(APIView):
    def get(self, request, recipe_id):
        try:
            nutrition_info = NutritionInfo.objects.get(recipe_id=recipe_id)
            serializer = NutritionInfoSerializer(nutrition_info)
            return Response(serializer.data)
        except NutritionInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)