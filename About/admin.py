from datetime import datetime

from django.contrib import admin

# Register your models here.
from About.models import AboutModel


class AboutAdmin(admin.ModelAdmin):
    list_display = ('Sno','BannerImage',
                    'Title','Content', 'is_active',
                    'ModifiedDate',
                    'CreatedDate',
                    'ModifiedBy',)

    search_fields = ('Sno','BannerImage',
                    'Title','Content','is_active',)

    exclude = ('ModifiedDate', 'added_by', 'ModifiedBy',)

    def save_model(self, request, obj, form, change):
        obj.ModifiedBy = str(request.user)
        obj.ModifiedDate = datetime.now()
        obj.save()

    def has_delete_permission(self, request, obj=None):
        print(obj)
        # if obj != None:
        #     data = LogoModel.objects.filterby(obj).values('is_active')
        #     if data[0]['is_active']:
        #         return True
        return True

    def delete_model(modeladmin, request, queryset):
        queryset.is_active = False
        queryset.save()

admin.site.register(AboutModel,AboutAdmin)