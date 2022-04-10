from rest_framework import generics
from .serializers import RecipesSerializer
from .models import Recipes

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# class RecipesView(APIView):
#     queryset = Recipes.objects.all()
#     serializer_class = RecipesSerializer

class RecipesView(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
