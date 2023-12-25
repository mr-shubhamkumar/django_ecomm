from importlib.resources import path

from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view 
from django.contrib.auth import logout
from .forms import LoginForm ,MyPasswordForm, MyPasswordResetForm, MySetPasswordForm
# myworld\Scripts\activate.bat
urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('cart-item/', views.cart_item, name='cart-item'),
    path('plus-cart/',views.plus_cart, name='plus-cart'),
    path('minus-cart/',views.minus_cart, name='minus-cart'),
    path('remove-cart/',views.remove_cart, name='remove-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),


    # All Auth Section Start
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm,), name='login'),

     path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),

    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordForm, success_url='/password-change-done/'), name='passwordchange'),

    path('password-change-done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password-change-done.html'), name='password_change_done'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

      path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
# All Auth Section End

    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),

    path('mobile/', views.mobile, name='mobile'),

    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('laptop/', views.laptop, name='laptop'),

    path('laptop/<slug:data>', views.laptop, name='laptopdata'),

    path('top-wear/', views.topwear, name='topwear'),

    path('top-wear/<slug:data>', views.topwear, name='topweardata'),

    path('botttom-wear/', views.bottomwear, name='botttomwear'),

    path('botttom-wear/<slug:data>', views.bottomwear, name='botttomweardata'),






    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
