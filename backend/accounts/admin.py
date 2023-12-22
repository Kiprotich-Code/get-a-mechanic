from django.contrib import admin
from . models import CustomUser, Profile
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = ProfileForm
    form = UserRegisterForm
    model = CustomUser
    list_display = ("email", "full_names", "is_active",)
    list_filter = ("email", "full_names", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "full_names", "user_type", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
