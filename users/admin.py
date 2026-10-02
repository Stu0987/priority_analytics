from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


from .models import User




@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "last_login",
        "date_joined",
    )


    search_fields = ("username", "email")
    ordering = ("-date_joined",)


    fieldsets = DjangoUserAdmin.fieldsets
    add_fieldsets = DjangoUserAdmin.add_fieldsets

