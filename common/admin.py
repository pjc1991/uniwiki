from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from common.models import UniUser


# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):
    """
    Base model admin
    """
    readonly_fields = (
        'id',
        'created_at',
        'modified_at',
    )

    # list display str

    list_display = (
        '__str__',
        'id',
        'created_at',
        'modified_at',
    )

    list_filter = (
        'created_at',
        'modified_at',
    )

    ordering = (
        '-created_at',
    )


class UniUserModelAdmin(UserAdmin):
    """
    Custom user model admin
    """

    # There is nothing to customize for now
    # However, we can add more fields here when needed

    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets


admin.site.register(UniUser, UniUserModelAdmin)
