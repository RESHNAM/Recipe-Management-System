from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView, View
from django.http import JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class HomeView(ListView):
    model = Recipe
    paginate_by = 10
    template_name = "home.html"

class RecipeDetailView(DetailView):
    """
    Retrieve, update or delete an recipe instance.
    """
    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404
        

    def get(self, request, pk, format=None):
        
        # recipe_id = self.kwargs['slug']
        recipe_id = self.get_object(pk)
        # serializer = RecipeSerializer(recipe_id, context={'request': request})
        # data = serializer.data
        # refined_data = JsonResponse(data)
        # print("DATA: ",refined_data)


        # return render(refined_data, 'detail.html', status=status.HTTP_200_OK)

        recipe = Recipe.objects.get(pk=recipe_id)

        print("RECIPE: ",recipe)

        context = {
            'object': recipe
        }

        return render(self.request, 'detail.html', context)
    
    # def get(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     serializer = UserSerializer(user, context={'request': request})
    #     return Response(serializer.data, status=status.HTTP_200_OK)