from django.db import models

import uuid

from django.core.signals import request_finished
from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
                                        )

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class UserManager(BaseUserManager):
    def create_user(self,email,userName,password=None,is_active = True,is_member=False,is_admin = False):
        if not email:
            raise  ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have an Password!")
        user = self.model(
            userName = userName,
            email =  self.normalize_email(email)
        )

        user.is_admin = is_admin
        user.is_member = is_member
        user.is_active =  is_active
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_memberuser(self,email,userName,password= None):
        user = self.create_user(email,userName,
                                password= password,
                                is_member=True,
                                is_active = True
                                )
        return user

    def create_superuser(self, email,userName, password=None):
        user = self.create_user(email,userName,
                                password= password,
                                is_admin=True
                                )

        return user


class User(AbstractBaseUser,PermissionsMixin):
    UserID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=255,primary_key=True, verbose_name='E-mail address')
    userName = models.CharField(max_length= 255)
    is_admin =  models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_member =  models.BooleanField(default= False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userName']

    def __str__(self):
        return  self.email

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        db_table = 'Userdetails'
        verbose_name = 'User  List'
        verbose_name_plural = 'User List'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.filter(user=instance).delete()
        Token.objects.create(user=instance)

