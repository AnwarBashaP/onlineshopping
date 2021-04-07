from rest_framework.authtoken.models import Token

from Home.models import User
from LandingPage.models import LogoModel
from Product.models import MainClassProductNav, SubClassProductNav, CartModel


def home(request):
    Data = LogoModel.objects.filter(is_active=True).all().order_by('-CreatedDate')[:1]
    NavBarHeading= MainClassProductNav.objects.filter(is_active=True).all()
    ProductMenus = []
    data= []
    if Data:
        for i in Data:
            data.append({"Logo":i.Logo.url,"Alt":i.Alt,"CallUs":i.CallUs})

    if NavBarHeading:
        for i in NavBarHeading:
            ProID =  i.Sno
            ProTitle = i.ProductTitle
            ProductData = SubClassProductNav.objects.filter(is_active=True, MainProductID=ProID).all()
            if ProductData:
                ProductSubMenus = []
                for M in ProductData:
                    ProductSubMenus.append({M.Sno:M.ProductTitle})
            ProductMenus.append({i: ProductSubMenus})
    Count = None

    if 'token' in request.session:
        token = Token.objects.get(key=request.session['token'])
        CartDataCount = CartModel.objects.filter(User=User.objects.get(pk=token.user_id)).count()
        if CartDataCount:
            Count = CartDataCount
    # Submenu = SubClassProductNav.objects.filter(is_active=True,MainProductID = MainClassProductNav.objects.filter(is_active=True).all()).all()

    output ={
    'NavHead':ProductMenus,
    "logo":data,
    "Count":Count
    }
    return output