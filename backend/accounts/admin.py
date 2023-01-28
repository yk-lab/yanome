from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # add_form_template = 'admin/auth/user/add_form.html'
    # change_user_password_template = None
    readonly_fields = (
        # 'created',
        # 'modified',
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ()}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        # (_('Important dates'), {
        #  'fields': ('last_login', 'created', 'modified')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email',),
            },
        ),
    )
    # form = UserChangeForm
    # add_form = UserCreationForm
    # change_password_form = AdminPasswordChangeForm
    list_display = ('email',)
    list_filter = ('is_superuser', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = (
        'groups',
        'user_permissions',
    )
