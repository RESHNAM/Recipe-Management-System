from django.forms import ModelForm
from .models import Recipe
from django.template.defaultfilters import slugify


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'