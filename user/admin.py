from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserAdmin

from . import models
# from .models import Author, User
from .models import User
# admin.site.register(models.Author)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "first_name", "last_name","email","phone"),
            },
        ),
    )
    list_display = ['first_name', 'last_name', 'email', 'phone']
    list_display_links = ['email']
    list_editable = ['first_name', 'last_name', 'phone']
    list_per_page = 10


# @admin.register(Author)
# class AuthorAdmin(BaseUserAdmin):
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "usable_password", "password1", "password2", "first_name", "last_name","email","phone", "dob"),
#             },
#         ),
#     )
#     list_display = ['first_name', 'last_name', 'email', 'phone','dob', 'dod']
#     list_display_links = ['email','dob', 'dob']
#     list_editable = ['first_name', 'last_name', 'phone']
#     list_per_page = 10