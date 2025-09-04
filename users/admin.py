from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(User)
class Admin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Extra Info", {"fields": ("role", "avatar","phone_number", "bio", "job", "resume", "location", "github", "linkedin", "website")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Extra Info", {"fields": ("role", "avatar", "phone_number","bio", "job", "resume", "location", "github", "linkedin", "website")}),
    )
