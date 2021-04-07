import os
from datetime import datetime as dt
import  datetime
from io import BytesIO

from PIL.Image import Image, logger
from django.db import models

# Create your models here.
from django.dispatch import receiver
from django_resized import ResizedImageField

from Ecommerce import settings
from Product.models import SubClassProductNav, update_ProductCat


def update_Logo(instance, filename):
    today = datetime.date.today()
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    mainpath = 'Logo/'
    path = str(instance.Alt)
    ext = filename.split('.')[-1]
    filename = '{}{}.{}'.format(today,current_time,ext)

    return os.path.join(mainpath, path, filename)



class LogoModel(models.Model):
    SNo = models.AutoField(primary_key=True)
    Logo = ResizedImageField(size=[180, 200],quality=100,upload_to=update_Logo,max_length=255,force_format='PNG')
    Alt =  models.CharField(max_length=100)
    CallUs = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'Logo'
        verbose_name = 'Logo List'
        verbose_name_plural ='Logo List'

    def __str__(self):
        return str(self.SNo)


    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)






class HeaderLinkGenerateModel(models.Model):
    Sno = models.AutoField(primary_key=True)
    Content =  models.CharField(max_length=200)
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'HeaderLinkGenerate'
        verbose_name = 'HeaderLinkGenerate List'
        verbose_name_plural = 'HeaderLinkGenerate List'

    def __str__(self):
        return self.Content

    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)


def update_Banner(instance, filename):
    today = datetime.date.today()
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    mainpath = 'Banner/'
    ext = filename.split('.')[-1]
    filename = '{}{}.{}'.format(today,current_time,ext)
    return os.path.join(mainpath, filename)

class BannerModel(models.Model):
    Sno = models.AutoField(primary_key=True)
    Heading = models.CharField(max_length=200)
    # Banner = ResizedImageField(size=[1920, 1000], quality=100, upload_to=update_Banner, max_length=255, force_format='JPEG')
    Description = models.CharField(max_length=255)
    Link = models.URLField()
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'Banner'
        verbose_name = 'Banner List'
        verbose_name_plural = 'Banner List'

    def __str__(self):
        return self.Heading
    #
    # def get_absolute_image_url(self):
    #     return os.path.join(settings.MEDIA_URL, self.Banner.url)

    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)



class BannerImagesModel(models.Model):
    Sno = models.AutoField(primary_key=True)
    HeaderID = models.ForeignKey(BannerModel,on_delete=models.CASCADE)
    Banner = ResizedImageField(size=[1920, 1000], quality=100, upload_to=update_Banner, max_length=255, force_format='JPEG')
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'BannerImages'
        verbose_name = 'BannerImages List'
        verbose_name_plural = 'BannerImages List'

    def __str__(self):
        return str(self.HeaderID)

    def get_absolute_image_url(self):
        return os.path.join(settings.MEDIA_URL, self.Banner.url)

    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)



def update_ProductCat(instance, filename):
    today = datetime.date.today()
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    mainpath = 'ProductCat/'
    filpath =  instance.ProductTitle
    ext = filename.split('.')[-1]
    filename = '{}{}.{}'.format(today,current_time,ext)
    return os.path.join(mainpath,filpath, filename)

class HomeProductCatModel(models.Model):
    Sno = models.AutoField(primary_key=True)
    ProductTitle = models.CharField(max_length= 255)
    SubProductID = models.ForeignKey(SubClassProductNav, on_delete=models.CASCADE)
    ProductImage = ResizedImageField(size=[500, 500], quality=100, upload_to=update_ProductCat, max_length=255, force_format='JPEG')
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'HomeProductCat'
        verbose_name = 'HomeProductCat List'
        verbose_name_plural = 'HomeProductCat List'

    def __str__(self):
        return str(self.ProductTitle)

    def get_absolute_image_url(self):
        return os.path.join(settings.MEDIA_URL, self.Banner.url)

    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)


@receiver(models.signals.pre_save, sender=HomeProductCatModel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False
    try:
        old_file = HomeProductCatModel.objects.get(pk=instance.Sno).ProductImage
    except HomeProductCatModel.DoesNotExist:
        return False
    new_file = instance.ProductImage
    # old_file = instance.ProductImage
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove( old_file.path)


@receiver(models.signals.pre_save, sender=BannerImagesModel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False
    try:
        old_file = BannerImagesModel.objects.get(pk=instance.Sno).Banner
    except BannerImagesModel.DoesNotExist:
        return False
    new_file = instance.Banner
    # old_file = instance.ProductImage
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove( old_file.path)


@receiver(models.signals.pre_save, sender=LogoModel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = LogoModel.objects.get(pk=instance.Sno).Logo
    except LogoModel.DoesNotExist:
        return False
    new_file = instance.Logo
    # old_file = instance.ProductImage
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove( old_file.path)






def update_Ads(instance, filename):
    today = datetime.date.today()
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    mainpath = 'BoxAds/'
    # filpath =  instance.ProductTitle
    ext = filename.split('.')[-1]
    filename = '{}{}.{}'.format(today,current_time,ext)
    return os.path.join(mainpath, filename)




class BoxAdModel(models.Model):
    Sno = models.AutoField(primary_key=True)
    AdImage = ResizedImageField(size=[570, 326], quality=100, upload_to=update_Ads, max_length=255, force_format='JPEG')
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'BoxAds'
        verbose_name = 'BoxAds List'
        verbose_name_plural = 'BoxAds List'

    def __str__(self):
        return str(self.Sno)

    def get_absolute_image_url(self):
        return os.path.join(settings.MEDIA_URL, self.Banner.url)

    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)


@receiver(models.signals.pre_save, sender=BoxAdModel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = BoxAdModel.objects.get(pk=instance.Sno).AdImage
    except BoxAdModel.DoesNotExist:
        return False
    new_file = instance.AdImage
    # old_file = instance.ProductImage
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove( old_file.path)


