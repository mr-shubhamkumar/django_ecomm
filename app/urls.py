from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm
# myworld\Scripts\activate.bat
urlpatterns = [
    path('',views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    # path('login/', views.login, name='login'),
    path('top-wear/', views.topwear, name='topwear'),
    path('top-wear/<slug:data>', views.topwear, name='topweardata'),
    path('botttom-wear/', views.bottomwear, name='botttomwear'),
    path('botttom-wear/<slug:data>', views.bottomwear, name='botttomweardata'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('registration/',views.CustomerRegistrationView.as_view(),name="customerregistration"),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
