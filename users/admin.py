from .models import User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models


# Register your models here.
class UserAdminConfig(UserAdmin):
    model = User
    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name'
    )
    list_filter = (
        'email',
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
    ordering = ('created_on',)
    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'email',
                    'username',
                    'first_name',
                    'last_name'
                )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 20,
                'cols': 60
            })
        },
    }
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'username',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                    'is_active',
                    'is_staff'
                )
            }
        )
    )


admin.site.register(User, UserAdminConfig)
