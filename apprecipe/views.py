from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView, View

from.models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class HomeView(ListView):
    model = Recipe
    paginate_by = 10
    template_name = "home.html"