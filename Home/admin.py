from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)
from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email','userName','is_admin','is_active','is_member',)
    exclude =  ('last_login','groups','user_permissions','password',)
    actions = ['delete','Hard_Delete']

    def has_delete_permission(self, request, obj=None):

        if obj != None:
            data = User.objects.filter(email__exact=obj).values('is_active')
            if data[0]['is_active']:
                return True
        return False
    def delete_model(modeladmin, request, queryset):
        queryset.is_active = False
        queryset.save()

    def Hard_Delete(modeladmin, request, queryset):
        for mail in queryset:
            if mail:
                User.objects.filter(email=mail).update(is_active =  False)
admin.site.register(User,UserAdmin)