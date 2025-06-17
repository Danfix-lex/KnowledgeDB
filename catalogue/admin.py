from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'language', 'isbn']
    list_filter = ['isbn']
    search_fields = ['title']

admin.site.register(models.Book)
admin.site.register(models.Language)
admin.site.register(models.Genre)