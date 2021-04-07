from django.db.models import Q
from rest_framework import serializers, status

from Ecommerce.CustomValidationError import CustomValidation
from Home.models import User
from LandingPage.models import BannerImagesModel, BannerModel, HomeProductCatModel


class UserLoginSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(allow_blank=True,read_only=True)
    email = serializers.EmailField(label="Email Address",required=False,allow_blank=True)

    class Meta:
        model = User
        fields = ('email', 'userName', 'password')
        extra_kwargs = {"password":
            {"write_only":True}
                        }
    def validate(self,data):
        email =  data.get("email",None)

        # username = data.get("userName",None)
        password = data.get("password",None)
        if not email:
            raise CustomValidation("A username must!","UserName", status_code=status.HTTP_401_UNAUTHORIZED)


        user = User.objects.filter(
                email= email
            ).exclude(Q(email__isnull=True)
            ).exclude(Q(email__iexact='')
            ).distinct()

        # print(user)

        # user exists
        if user.exists() and user.count() == 1:
            user_obj = user.first()
            if not user_obj.is_active:
                raise CustomValidation("User is not active!","User", status_code=status.HTTP_401_UNAUTHORIZED)

        else:
            raise CustomValidation( "Invalid Credentials!","Email", status_code=status.HTTP_401_UNAUTHORIZED)

        if user_obj:
            if not user_obj.check_password(password):
                raise CustomValidation( "Invalid Credentials!","Password", status_code=status.HTTP_401_UNAUTHORIZED)
        return data

class Bannerseralizer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = ('Heading', 'Description','Link')


class HomeProductCat(serializers.ModelSerializer):
    # image_url = serializers.URLField(source='get_absolute_image_url', read_only=True)
    class Meta:
        model = HomeProductCatModel
        fields = ('ProductTitle', 'ProductImage','Link')


class BannerImageSerializer(serializers.ModelSerializer):

    image_url = serializers.URLField(source='get_absolute_image_url', read_only=True)
    HeaderID = Bannerseralizer()
    class Meta:
        model = BannerImagesModel
        fields = ('Banner', 'image_url','HeaderID')

