from django.contrib import admin
from .models import Recipe

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'meal_type',
        'calories',
        'instruction',
        'ingredients',
        'images'
    )
    list_filter = ('meal_type',)
