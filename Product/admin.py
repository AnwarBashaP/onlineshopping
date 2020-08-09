from datetime import datetime

from django.contrib import admin

# Register your models here.
from Product.models import MainClassProductNav, SubClassProductNav, ProductDetails, InduvialProductDetails, \
    InduvialProductReviews, InduvialProductImages, CartModel


class MainProductAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'ProductTitle', 'is_active',
                    'ModifiedDate',
                    'CreatedDate',
                    'ModifiedBy',)

    search_fields = ('Sno', 'ProductTitle', 'is_active',)

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


class SubProductAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'MainProductID', 'ProductTitle', 'is_active',
                    'ModifiedDate',
                       'CreatedDate',
                    'ModifiedBy',)

    search_fields = ('Sno', 'MainProductID__ProductTitle', 'ProductTitle', 'is_active',)

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


class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('Sno','Is_Spl','slug', 'SubProductID','SplList','Offer','ProductImage','ProductTitle','StrikePrice','Price', 'is_active',
                    'ModifiedDate','CreatedDate','ModifiedBy',)

    search_fields = (
    'Sno','Is_Spl','slug', 'SubProductID__ProductTitle','SplList','Offer','ProductImage','ProductTitle','StrikePrice','Price','is_active',)

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


class InduvialProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'ProductID','Description','AvalibleNo', 'is_active',
                    'ModifiedDate','CreatedDate','ModifiedBy',)

    search_fields = (
    'Sno', 'ProductID__ProductTitle', 'ProductID','Description','AvalibleNo','is_active',)

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

class InduvialProductReviewsAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'ProductID','Reviews','is_active',
                    'ModifiedDate','CreatedDate','ModifiedBy',)

    search_fields = (
    'Sno', 'ProductID__ProductTitle', 'ProductID','Reviews','is_active',)

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


class InduvialProductImagesAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'ProductID','ProductImage','is_active',
                    'ModifiedDate','CreatedDate','ModifiedBy',)

    search_fields = (
    'Sno', 'ProductID__ProductTitle', 'ProductID','ProductImage','is_active',)

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

class CartModelAdmin(admin.ModelAdmin):
    list_display = ('Sno','ProductID','User', 'Total', 'is_active',
                    'ModifiedDate','CreatedDate','ModifiedBy',)

    # search_fields = (
    # 'Sno','Is_Spl','slug', 'SubProductID__ProductTitle','SplList','Offer','ProductImage','ProductTitle','StrikePrice','Price','is_active',)

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



admin.site.register(MainClassProductNav, MainProductAdmin)
admin.site.register(SubClassProductNav, SubProductAdmin)
admin.site.register(ProductDetails, ProductDetailsAdmin)
admin.site.register(InduvialProductDetails, InduvialProductDetailsAdmin)
admin.site.register(InduvialProductReviews, InduvialProductReviewsAdmin)
admin.site.register(InduvialProductImages, InduvialProductImagesAdmin)
admin.site.register(CartModel, CartModelAdmin)
