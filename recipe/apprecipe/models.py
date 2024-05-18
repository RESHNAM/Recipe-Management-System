from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    CATEGORY_CHOICES = (
        ('amateur', 'amateur'),
        ('regular', 'regular'),
        ('professional', 'professional')
    )
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} : {}".format(self.title, self.description)
