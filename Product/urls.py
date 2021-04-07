from django.urls import path

from .views import OverAllProductView, InduvialProductView, AddToCart, whishlistView, whistlistProductview, \
    CartProductView, CartUpdate

urlpatterns = [
    path('overallproduct/<mainproduct>/', OverAllProductView, name='overallProduct'),
    path('induvialProduct/<product>/', InduvialProductView, name='induvialProduct'),
    path('whishlist/', whishlistView, name='whishlist'),
    path('cartupdate/', CartUpdate, name='CartUpdate'),
    path('cartview/', CartProductView, name='cartview'),
    path('whishpage/', whistlistProductview, name='whishlist'),
    path('addtocart/<slug>', AddToCart, name='AddToCart View'),
#     path('signup', signupView.as_view(), name='SignUp Page'),
#     path('login', loginView, name='Login Page'),
#     path('logout', User_LogoutAPIView, name='Logout Page'),
]