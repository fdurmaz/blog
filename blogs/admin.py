from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'created_date', 'updated_date', 'categories')
    readonly_fields = ('created_date', 'updated_date')

    list_display = ('title', 'created_date', 'updated_date')
    search_fields = ('title', 'categories')
    filter_horizontal = ('categories',)

