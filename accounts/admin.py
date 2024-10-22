from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'room_id', 'intermission']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('room_id', 'intermission')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('room_id', 'intermission')}),
    )


admin.site.register(CustomUser, CustomerUserAdmin)
