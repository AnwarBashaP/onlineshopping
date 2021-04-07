import re
from decimal import Decimal

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from six import text_type
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.base import View
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, api_view, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from Home.models import User
from Product.models import ProductDetails, InduvialProductDetails, InduvialProductImages, CartModel


@permission_classes((AllowAny,))
# @permission_classes([IsAuthenticated])
# @api_view(["POST"])
@csrf_exempt
# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def OverAllProductView(request, mainproduct):
    template_name = 'Product/product.html'
    if request.is_ajax():
        priceRange = request.POST['prize']
        alternativefilter = request.POST['alternativefilter']
        searchvalues = request.POST['searchfilter']
        prize = priceRange.split('-')
        if searchvalues == 'None':
            queryset = ProductDetails.objects.filter(is_active=True, SubProductID=mainproduct, Price__range=(
                Decimal(str(prize[0]).replace('$', '')), Decimal(str(prize[1]).replace('$', '')))).all().order_by(
                '-CreatedDate')
        else:
            queryset = ProductDetails.objects.filter((Q(ProductTitle__icontains=searchvalues) | Q(Offer__icontains
                                                                                                  =searchvalues) | Q(
                SplList__icontains=searchvalues) | Q(
                SubProductID__ProductTitle__icontains
                =searchvalues)), is_active=True, SubProductID=mainproduct, Price__range=(
                Decimal(str(prize[0]).replace('$', '')),
                Decimal(str(prize[1]).replace('$', '')))).all().order_by(
                '-CreatedDate')

        data = []
        if queryset:
            for i in queryset:
                data.append({"Offer": i.Offer, "ProductImage": i.ProductImage.url, "slug": i.slug,
                             "ProductTitle": i.ProductTitle, "StrikePrice": i.StrikePrice, "Price": i.Price,
                             "Description": i.Description})

            if alternativefilter == '1':
                data = sorted(data, key=lambda e: e['Price'], reverse=True)
            elif alternativefilter == '2':
                data = sorted(data, key=lambda e: e['Price'], reverse=False)

            context = {"products": data, "count": len(data), "RangeStart": int(str(prize[0]).replace('$', '')),
                       "RangeEnd": int(str(prize[1]).replace('$', '')), "Alternativefilter": int(alternativefilter)}

        else:
            context = {"products": None, "count": None, "RangeStart": None, "RangeEnd": None, "Alternativefilter": '0'}

        return JsonResponse(context)

    else:
        queryset = ProductDetails.objects.filter(is_active=True, SubProductID=mainproduct).all().order_by(
            '-CreatedDate')
        if queryset:

            context = {"products": queryset, "count": len(queryset), "RangeStart": None, "RangeEnd": None,
                       "Alternativefilter": '0'}
        else:
            context = {"products": None, "count": None, "RangeStart": None, "RangeEnd": None, "Alternativefilter": '0'}

        return render(request, template_name, context=context)


@permission_classes((AllowAny,))
# @permission_classes([IsAuthenticated])
def InduvialProductView(request, product):
    template_name = 'Product/shop-details.html'
    queryset = ProductDetails.objects.filter(is_active=True, slug__iexact=product).all().order_by('-CreatedDate')
    images = InduvialProductImages.objects.filter(is_active=True,
                                                  ProductID__in=ProductDetails.objects.filter(is_active=True,
                                                                                              slug__icontains=product).values(
                                                      'Sno')).all().order_by('-CreatedDate')

    if queryset:

        context = {"productData": queryset, "images": images}
    else:
        context = {"productData": None, "images": None}
    print(context)
    return render(request, template_name, context=context)


@permission_classes((AllowAny,))
# @permission_classes([IsAuthenticated])
@csrf_exempt
def whishlistView(request):
    template_name = 'Product/product.html'
    products = request.POST['items']
    listofproduct = products.split(',')[1:]
    whishlistproduct = []
    queryset = ProductDetails.objects.filter(is_active=True, slug__in=listofproduct).all().order_by('-CreatedDate')
    for i in queryset:
        InStock = 'Out of Stock'
        if i.AvalibleNo != 0:
            InStock = 'In Stock'
        whishlistproduct.append(
            {"PrImages": i.ProductImage.url, "ProductTitle": i.ProductTitle, "Price": i.Price,
             "Stock": InStock, "slug": i.slug})

    if queryset:

        context = {"productData": whishlistproduct}
    else:
        context = {"productData": None}

    return JsonResponse(context)


@permission_classes((AllowAny,))
@csrf_exempt
# @permission_classes([IsAuthenticated])
# @require_http_methods([ "POST"])
def AddToCart(request, slug):
    try:
        token = Token.objects.get(key=request.session['token'])
        if slug != "None":
            CartData = CartModel.objects.filter(User=User.objects.get(pk=token.user_id)).all()

            if CartData:
                preOrder = CartData.filter(ProductID=ProductDetails.objects.get(slug=slug)).values('Total')
                if preOrder:
                    Total = preOrder[0]['Total'] + 1

                    preOrder.update(Total=Total)
                else:
                    CartData.create(User=User.objects.get(pk=token.user_id), ProductID=ProductDetails.objects.get(slug=slug),
                                    Total=1)

            else:

                CartData.create(User=User.objects.get(pk=token.user_id), ProductID=ProductDetails.objects.get(slug=slug),
                                Total=1)

            CartDataCount = CartModel.objects.filter(User=User.objects.get(pk=token.user_id)).count()
            return JsonResponse({"Count": CartDataCount,  "status": "pass"})
        else:
            OutputData = []
            CartDataProduct = CartModel.objects.filter(User=User.objects.get(pk=token.user_id)).values(
                'ProductID__ProductTitle', 'Total', 'ProductID__Price', 'ProductID__slug','ProductID__ProductImage')
            priceamount = []
            checkouttotal = []
            for i in CartDataProduct:
                priceamount.append(int(i['ProductID__Price']))
                totalprice = int(i['Total'])*int(i['ProductID__Price'])
                checkouttotal.append(int(i['Total'])*int(i['ProductID__Price']))
                OutputData.append(
                    {"ProductTitle": i['ProductID__ProductTitle'], "Total": i['Total'], "Price": i['ProductID__Price'],
                     "slug": i['ProductID__slug'],"ProductImage":"media/"+i['ProductID__ProductImage'],"TotalPriceAmount":totalprice})
            print(checkouttotal)
            return JsonResponse({"OutputData": OutputData,"Totalamount":sum(priceamount),"Checkout":sum(checkouttotal), "status": "pass"})

    except:
        return JsonResponse({"message":"Success"})



@permission_classes((AllowAny,))
# @permission_classes([IsAuthenticated])
def whistlistProductview(request):

    template_name = 'Product/wishlist.html'
    return render(request, template_name)

@permission_classes((AllowAny,))
# @permission_classes([IsAuthenticated])
def CartProductView(request):
    template_name = 'Product/Cart.html'
    return render(request, template_name)




@permission_classes((AllowAny,))
@csrf_exempt
# @permission_classes([IsAuthenticated])
def CartUpdate(request):
    UserSession = request.session['token']
    datas = eval(request.POST['dataset'])
    token = Token.objects.get(key=request.session['token'])
    print(datas)
    for data in datas:
        slugid = data['slug']
        sludvalid = ProductDetails.objects.filter(slug = slugid).values('Sno')
        slugid = sludvalid[0]['Sno']
        total = data['qty']
        CartData = CartModel.objects.filter(User=User.objects.get(pk=token.user_id),ProductID = slugid).update(Total = total)

    OutputData = []
    CartDataProduct = CartModel.objects.filter(User=User.objects.get(pk=token.user_id)).values(
        'ProductID__ProductTitle', 'Total', 'ProductID__Price', 'ProductID__slug', 'ProductID__ProductImage')
    priceamount = []
    checkouttotal = []
    for i in CartDataProduct:
        priceamount.append(int(i['ProductID__Price']))
        totalprice = int(i['Total']) * int(i['ProductID__Price'])
        checkouttotal.append(int(i['Total']) * int(i['ProductID__Price']))
        OutputData.append(
            {"ProductTitle": i['ProductID__ProductTitle'], "Total": i['Total'], "Price": i['ProductID__Price'],
             "slug": i['ProductID__slug'], "ProductImage": "media/" + i['ProductID__ProductImage'],
             "TotalPriceAmount": totalprice})
    print(OutputData)