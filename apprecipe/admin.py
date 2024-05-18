from django.contrib import admin
from .models import *

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'ingredients',
        'instructions',
        'category',
        'created_at',
        'updated_at'
    ]
    list_filter = ['title', 'category', 'created_at']
    search_fields = ['title', 'category', 'created_at']

admin.site.register(Recipe, RecipeAdmin)
