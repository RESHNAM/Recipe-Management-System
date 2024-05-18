from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # path('', views.index, name='index',),
    path('', views.HomeView.as_view(), name='index'),
    path('detail/<int:pk>/', views.RecipeDetailView.as_view(), name='detail-view'),
    path('post-detail/', views.RecipeAddView.as_view(), name='post-detail-view'),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)