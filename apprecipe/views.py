from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView, View
from django.http import JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from .forms import *

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
        recipe_id = self.get_object(pk)
        recipe = Recipe.objects.get(pk=recipe_id)

        context = {
            'object': recipe
        }

        return render(self.request, 'detail.html', context)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = RecipeSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RecipeAddView(View):
    def post(self, *args, **kwargs):
        form = RecipeForm(self.request.POST or None)
        if form.is_valid():
            
            title = form.cleaned_data.get('title')
            recipe = Recipe.objects.get(title=title, ordered=False)
            recipe.save()
            messages.success(self.request, "Successfully added a recipe")
            return redirect("apprecipe:checkoutpost-detail-view")
            
