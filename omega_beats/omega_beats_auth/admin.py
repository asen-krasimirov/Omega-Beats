from importlib._common import _

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from omega_beats.omega_beats_auth.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class OmegaBeatsUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions',),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'pk', 'is_staff',)
    list_filter = ('is_staff', 'is_superuser', 'groups',)
    search_fields = ('email',)
    ordering = ('email', 'pk')
    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
