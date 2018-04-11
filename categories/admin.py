from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'created_date', 'updated_date')
    readonly_fields = ('created_date', 'updated_date')

    list_display = ('title', 'created_date', 'updated_date')
    search_fields = ('title',)
