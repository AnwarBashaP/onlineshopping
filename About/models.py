import datetime
import os
from datetime import datetime as dt

from django.db import models

# Create your models here.
from django.dispatch import receiver
from django_resized import ResizedImageField

from Ecommerce import settings


def update_BannerImage(instance, filename):
    today = datetime.date.today()
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    mainpath = 'About/Banner/'
    ext = filename.split('.')[-1]
    filename = '{}{}.{}'.format(today,current_time,ext)
    return os.path.join(mainpath, filename)

class AboutModel(models.Model):
    Sno =  models.AutoField(primary_key=True)
    BannerImage = ResizedImageField(size=[1920, 1001], quality=100, upload_to=update_BannerImage, max_length=255, force_format='JPEG')
    Title = models.CharField(max_length=255)
    Content =  models.TextField()
    is_active = models.BooleanField(default=False, verbose_name='Active Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    ModifiedDate = models.DateTimeField(blank=True, null=True, verbose_name='Modified On')
    ModifiedBy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Modified By')

    class Meta:
        db_table = 'About'
        verbose_name = 'About List'
        verbose_name_plural = 'About List'

    def __str__(self):
        return self.Title


    def get_absolute_image_url(self):
        return os.path.join(settings.MEDIA_URL, self.BannerImage.url)

    def save_model(self, request, obj, form, change):
        obj.added_by = str(request.user)
        super().save_model(request, obj, form, change)

@receiver(models.signals.pre_save, sender=AboutModel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = AboutModel.objects.get(pk=instance.Sno).BannerImage
    except AboutModel.DoesNotExist:
        return False
    new_file = instance.BannerImage
    # old_file = instance.ProductImage
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove( old_file.path)