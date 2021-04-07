import datetime
import os

import string
from datetime import datetime as dt
import random
from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.utils.text import slugify
from django_resized import ResizedImageField

from Home.models import User


class MainClassProductNav(models.Model):
    Sno = models.AutoField(primary_key=True)
    ProductTitle = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'MainClassProduct'
        verbose_name = 'MainClassProduct List'
        verbose_name_plural = 'MainClassProduct List'

    def __str__(self):
        return str(self.ProductTitle)

    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)

class SubClassProductNav(models.Model):
    Sno = models.AutoField(primary_key=True)
    MainProductID =  models.ForeignKey(MainClassProductNav,on_delete=models.CASCADE)
    ProductTitle = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'SubClassProduct'
        verbose_name = 'SubClassProduct List'
        verbose_name_plural = 'SubClassProduct List'

    def __str__(self):
        return str(self.ProductTitle)

    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)


def update_ProductCat(instance, filename):
    today = datetime.date.today()
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    mainpath = 'Product/'

    filpath =  str(instance.SubProductID)

    ext = filename.split('.')[-1]
    filename = '{}{}.{}'.format(instance.ProductTitle,current_time,ext)
    return os.path.join(mainpath, filpath, filename)

SplList = (
    ('tf','Top-Featured'),
    ('bs','Best-Seller'),
    ('hd','Hot-Deal')
)

class ProductDetails(models.Model):
    Sno = models.AutoField(primary_key=True)
    SubProductID =  models.ForeignKey(SubClassProductNav,on_delete=models.CASCADE)
    Is_Spl = models.BooleanField(default=False, verbose_name='Is_the_ProductSpllist')
    SplList = models.CharField(max_length=200, choices=SplList)
    Offer = models.CharField(max_length=240, verbose_name='Offer')
    ProductImage = ResizedImageField(size=[370, 350], quality=100, upload_to=update_ProductCat, max_length=255,
                                     force_format='JPEG')
    ProductTitle = models.CharField(max_length=200, verbose_name='Product Title')
    slug = models.SlugField(max_length=250, null=True, blank=True,unique=True)
    StrikePrice = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Strike Price', blank=True,
                                                                                                    null=True)
    Description = models.TextField(verbose_name='Descriptions')
    AvalibleNo = models.IntegerField()
    Price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Product Price')
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'ProductDetails'
        verbose_name = 'ProductDetails List'
        verbose_name_plural = 'ProductDetails List'

    def __str__(self):
        return str(self.ProductTitle)

    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)

@receiver(models.signals.pre_save, sender=ProductDetails)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = ProductDetails.objects.get(pk=instance.Sno).ProductImage
    except ProductDetails.DoesNotExist:
        return False
    new_file = instance.ProductImage
    # old_file = instance.ProductImage
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove( old_file.path)
    # os.remove("media/" + str(old_file.ProductImage))
    # return new_file


class InduvialProductDetails(models.Model):
    Sno = models.AutoField(primary_key=True)
    ProductID =  models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    Description = models.TextField(verbose_name='Descriptions')
    AvalibleNo = models.IntegerField()
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'InduvialProductDetails'
        verbose_name = 'InduvialProductDetails List'
        verbose_name_plural = 'InduvialProductDetails List'

    def __str__(self):
        return str(self.ProductID)

class InduvialProductReviews(models.Model):
    Sno = models.AutoField(primary_key=True)
    ProductID =  models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    Reviews = models.TextField(verbose_name='Descriptions')
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'InduvialProductReviews'
        verbose_name = 'InduvialProductReviews List'
        verbose_name_plural = 'InduvialProductReviews List'

    def __str__(self):
        return str(self.ProductID)


def induvialProduct(instance, filename):
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    mainpath = 'InduvialProduct/'

    filpath =  str(instance.ProductID)
    ext = filename.split('.')[-1]
    filename = '{}{}.{}'.format(instance.ProductID,current_time,ext)
    return os.path.join(mainpath, filpath, filename)

class InduvialProductImages(models.Model):
    Sno = models.AutoField(primary_key=True)
    ProductID =  models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    ProductImage = ResizedImageField(size=[370, 350], quality=100, upload_to=induvialProduct, max_length=255,
                                     force_format='JPEG')
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'InduvialProductImages'
        verbose_name = 'InduvialProductImages List'
        verbose_name_plural = 'InduvialProductImages List'

    def __str__(self):
        return str(self.ProductID)

@receiver(models.signals.pre_save, sender=InduvialProductImages)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = ProductDetails.objects.get(pk=instance.Sno).ProductImage
    except ProductDetails.DoesNotExist:
        return False
    new_file = instance.ProductImage
    # old_file = instance.ProductImage
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

def random_string_generator(size = 10, chars =string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.ProductTitle)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

@receiver(models.signals.pre_save, sender=ProductDetails)
def Sulg_filed_generate(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class CartModel(models.Model):
    Sno = models.AutoField(primary_key=True)
    ProductID =  models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Total = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total number of product')
    is_active = models.BooleanField(default=True, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'Cart'
        verbose_name = 'Cart List'
        verbose_name_plural = 'Cart List'

    def __str__(self):
        return str(self.Sno)