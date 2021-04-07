from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from LandingPage.decorator import Loginverifications
from LandingPage.models import LogoModel, HeaderLinkGenerateModel, BannerModel, BannerImagesModel, HomeProductCatModel, \
    BoxAdModel
from LandingPage.serializer import BannerImageSerializer
from Product.models import ProductDetails


@permission_classes((AllowAny,))
# @permission_classes([IsAuthenticated])
class signupView(View):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)


@permission_classes((AllowAny,))
# @permission_classes([IsAuthenticated])
@Loginverifications
# class loginView(View):
#     template_name = 'login.html'
def loginView(request):
    return render(request, 'login.html')


def User_LogoutAPIView(request):
    # if request.method == 'get':

    if 'token' in request.session:
        del request.session['user']
        del request.session['token']
        response = redirect('/home')
    return response


# @permission_classes((AllowAny,))
# # @permission_classes([IsAuthenticated])
# class LandPageView(View):
#     # serializer_class = FolderModalViewSerilizer
#     # queryset = FolderModal.objects.filter(is_active=True).all()
#     # filter_backends = (DjangoFilterBackend,)
#     # filter_fields = ('FilesName' ,'return_id__ReturnId')


def homepageview(request):

    return redirect('/home')
def LandPageView(request):
    template_name = 'index.html'
    # try:

    Content = HeaderLinkGenerateModel.objects.filter(is_active=True).values('Content')
    Banner = BannerModel.objects.filter(is_active=True).values('Sno', 'Heading', 'Description', 'Link').order_by(
        '-CreatedDate')[:1]
    readserilizer = BannerImagesModel.objects.filter(HeaderID__in=BannerModel.objects.order_by('-CreatedDate')[:1],
                                                     is_active=True).values('Banner')
    ProductCat = HomeProductCatModel.objects.filter(is_active=True).values('ProductTitle', 'ProductImage','SubProductID')
    BoxAds = BoxAdModel.objects.filter(is_active=True).values('AdImage').order_by('-CreatedDate')[:2]
    SplList = ProductDetails.objects.filter(is_active=True,Is_Spl= True).all().order_by('-CreatedDate')
    SplListData = []
    if SplList:
        for i in SplList:
            SplListData.append({"id":i.Sno,"ProductTitle": i.ProductTitle, "SplList": i.SplList, "Offer": i.Offer,
                                "ProductImage": i.ProductImage,"StrikePrice":i.StrikePrice,"Price":i.Price})

    BNImage = []
    PrCat = []
    if Banner:
        BannerHeading = Banner[0]['Heading']
        BannerDescription =Banner[0]['Description']
        BannerLink =Banner[0]['Link']
    if readserilizer:
        for i in readserilizer:
            BNImage.append('media/' + i['Banner'])

    BoxAdsData = []
    if BoxAds:
        for i in BoxAds:
            BoxAdsData.append({"AdImage": "media/" + i['AdImage']})

    if ProductCat:
        for i in ProductCat:
            ProductImage = "media/" + i['ProductImage']

            PrCat.append({"ProductTitle": i['ProductTitle'], "ProductImage": ProductImage, "SubProductID": i['SubProductID']})

    context = {
        'BannerHeading': BannerHeading,
        'BannerDescription': BannerDescription ,
        'BannerLink': BannerLink,
        'BannerImages': BNImage,
        'BoxAds': BoxAdsData,
        'Content': Content,
        'ProductCat': PrCat,
        'SplProduct':SplList,
            }

    return render(request, template_name, context=context)
