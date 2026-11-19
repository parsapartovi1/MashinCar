from django.contrib import admin
from .models import (User)
#, Profile , Follow)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    readonly_fields = ("created_at", "last_update", "last_login")

    fieldsets = (
        ("Login Info", {
            "fields": ("number","password")
        }),
        ("Personal Info", {
            "fields": ("email",)
        }),
        ("Permissions", {
            "fields": ("is_active", "is_superuser","is_staff")
        }),
        ("Privacy", {
            "fields": ("is_private",)
        }),
        ("Dates", {
            "fields": ("last_login", "created_at", "last_update")
        })
    )

# admin.site.register(Profile)
# admin.site.register(Follow)