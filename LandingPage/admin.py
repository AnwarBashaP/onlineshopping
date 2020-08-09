from datetime import datetime

from django.contrib import admin

# Register your models here.
from LandingPage.models import LogoModel, HeaderLinkGenerateModel, BannerModel, BannerImagesModel, HomeProductCatModel, \
    BoxAdModel


class LogoModalAdmin(admin.ModelAdmin):
    list_display = ('SNo',
                    'Logo','Alt','CallUs', 'is_active',
                    'ModifiedDate',
                    'CreatedDate',
                    'ModifiedBy',)

    search_fields = ('SNo',
                    'Logo','Alt','CallUs', 'is_active',)

    exclude = ('ModifiedDate', 'added_by', 'ModifiedBy',)

    def save_model(self, request, obj, form, change):
        obj.ModifiedBy = str(request.user)
        obj.ModifiedDate = datetime.now()
        obj.save()

    def has_delete_permission(self, request, obj=None):

        return True

    def delete_model(modeladmin, request, queryset):
        queryset.is_active = False
        queryset.save()




class HeaderLinkGenerateModelAdmin(admin.ModelAdmin):
    list_display = ('Sno',
                    'Content', 'is_active',
                    'ModifiedDate',
                    'CreatedDate',
                    'ModifiedBy',)

    search_fields = ('Sno',
                    'Content', 'is_active',)

    exclude = ('ModifiedDate', 'added_by', 'ModifiedBy',)

    def save_model(self, request, obj, form, change):
        obj.ModifiedBy = str(request.user)
        obj.ModifiedDate = datetime.now()
        obj.save()

    def has_delete_permission(self, request, obj=None):

        return True

    def delete_model(modeladmin, request, queryset):
        queryset.is_active = False
        queryset.save()



class BannerModelAdmin(admin.ModelAdmin):
    list_display = ('Sno',
                    'Heading', 'is_active',
                    'ModifiedDate',
                    'CreatedDate',
                    'ModifiedBy',)

    search_fields = ('Sno','Heading' 'is_active',)

    exclude = ('ModifiedDate', 'added_by', 'ModifiedBy',)

    def save_model(self, request, obj, form, change):
        obj.ModifiedBy = str(request.user)
        obj.ModifiedDate = datetime.now()
        obj.save()

    def has_delete_permission(self, request, obj=None):

        return True

    def delete_model(modeladmin, request, queryset):
        queryset.is_active = False
        queryset.save()



class BannerImageModelAdmin(admin.ModelAdmin):
    list_display = ('Sno','HeaderID',
                    'Banner', 'is_active',
                    'ModifiedDate',
                    'CreatedDate',
                    'ModifiedBy',)

    search_fields = ('Sno','Banner','HeaderID__Heading' 'is_active',)

    exclude = ('ModifiedDate', 'added_by', 'ModifiedBy',)

    def save_model(self, request, obj, form, change):
        obj.ModifiedBy = str(request.user)
        obj.ModifiedDate = datetime.now()
        obj.save()

    def has_delete_permission(self, request, obj=None):

        return True

    def delete_model(modeladmin, request, queryset):
        queryset.is_active = False
        queryset.save()

class ProductCatAdmin(admin.ModelAdmin):
    list_display = ('Sno','ProductTitle',
                    'ProductImage','SubProductID', 'is_active',
                    'ModifiedDate',
                    'CreatedDate',
                    'ModifiedBy',)

    search_fields = ('Sno','ProductTitle',
                    'ProductImage','SubProductID__ProductTitle' 'is_active',)

    exclude = ('ModifiedDate', 'added_by', 'ModifiedBy',)

    def save_model(self, request, obj, form, change):
        obj.ModifiedBy = str(request.user)
        obj.ModifiedDate = datetime.now()
        obj.save()

    def has_delete_permission(self, request, obj=None):

        return True

    def delete_model(modeladmin, request, queryset):
        queryset.is_active = False
        queryset.save()

class BoxAdModelAdmin(admin.ModelAdmin):
    list_display = ('Sno',
                    'AdImage', 'is_active',
                    'ModifiedDate',
                    'CreatedDate',
                    'ModifiedBy',)

    search_fields = ('Sno',
                    'AdImage' 'is_active',)

    exclude = ('ModifiedDate', 'added_by', 'ModifiedBy',)

    def save_model(self, request, obj, form, change):
        obj.ModifiedBy = str(request.user)
        obj.ModifiedDate = datetime.now()
        obj.save()

    def has_delete_permission(self, request, obj=None):
        return True

    def delete_model(modeladmin, request, queryset):
        queryset.is_active = False
        queryset.save()



admin.site.register(BannerImagesModel, BannerImageModelAdmin)
admin.site.register(BannerModel, BannerModelAdmin)
admin.site.register(HeaderLinkGenerateModel, HeaderLinkGenerateModelAdmin)
admin.site.register(LogoModel, LogoModalAdmin)
admin.site.register(HomeProductCatModel, ProductCatAdmin)
admin.site.register(BoxAdModel, BoxAdModelAdmin)



