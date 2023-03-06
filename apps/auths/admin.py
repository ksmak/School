# Python
from typing import (
    Optional,
    Union,
    List,
    Tuple,
    Any
)

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.handlers.wsgi import WSGIRequest

# Project
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Custom user admin class."""
    list_display = (
        'email',
        'last_name',
        'first_name',
        'patronymic',
        'is_active'
    )
    list_filter = ('email', )
    search_fields = ('email', )
    fieldsets = (
        ('Personal data', {
            'classes': ('wide', ),
            'fields': (
                'email',
                'password',
                'last_name',
                'first_name',
                'patronymic'
            )
        }),
        ('Permissions', {
            'classes': ('wide', ),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups'
            )
        })
    )
    add_fieldsets = (
        ('Personal data', {
            'classes': ('wide', ),
            'fields': (
                'email',
                'password1',
                'password2',
                'last_name',
                'first_name',
                'patronymic'
            )
        }),
        ('Permissions', {
            'classes': ('wide', ),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        })
    )
    ordering = ('email', )
    readonly_fields = ('is_superuser', )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[CustomUser] = None
    ) -> tuple:
        if not obj:
            return self.readonly_fields
        
        return self.readonly_fields + ('email', )


admin.site.register(CustomUser, CustomUserAdmin)
