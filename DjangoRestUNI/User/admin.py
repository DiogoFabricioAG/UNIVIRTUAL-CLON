from django.contrib import admin    
from .models import User,FriendshipRequest
from django.contrib.auth.admin import UserAdmin

class UsersAdmin(UserAdmin):
    ordering = ('authcode',)
    list_display = ('last_name','first_name','role')
    add_fieldsets = (
        (None, {
            'fields': ('authcode', 'password1', 'password2','email' ,'role','first_name', 'last_name','avatar','city','country','description','is_active'),
        }),
    )
    fieldsets = (
        (None, {
            "fields": (
                'authcode',
                'password',
                'date_joined',
                'last_login',
            ),
        }),
    )
    

admin.site.register(User,UsersAdmin)
admin.site.register(FriendshipRequest) 