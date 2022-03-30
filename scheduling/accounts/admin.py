from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # todo : create user_creation form
    list_display = ('id', 'created_at', 'mobile', 'name', 'email', 'is_admin', 'is_superuser', 'is_active')
    fieldsets = (
    ('main', {'fields': ('email', 'mobile', 'profile_image')}),
    ('permissions', {'fields': ('is_active', 'last_login', 'groups', 'user_permissions', 'is_superuser')}),
    )
    ordering = ('created_at',)
    list_filter = ('is_admin', 'is_active', 'created_at')

    def get_form(self, request, obj=None, **kwargs):
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form
