from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from custom_user.models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class CustomUserAdmin(UserAdmin):
    # form = CustomUserChangeForm
    pass
    # fieldsets = UserAdmin.fieldsets + ((None, {'fields': (
    #     'display_name', 'password1', 'password2')}),)


admin.site.register(CustomUser, CustomUserAdmin)
