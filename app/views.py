from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationFrom, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect , HttpResponse
from .forms import LoginForm

from django.db.models import Q
from django.http import JsonResponse


# Product View in Home Page
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottompwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        return render(request, 'app/home.html',
                      {'topwears': topwears, 'bottompwears': bottompwears, 'mobiles': mobiles, 'laptop': laptop,
                       })


# Product Details Page
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        # print(product)
        return render(request, 'app/productdetail.html', {
            'product': product
        })


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        carts = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                tempamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {
                'carts': carts,
                'totalamount': tempamount,
                'amount': amount
            })
        else:
            return render(request, 'app/emptycart.html')

           



def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]

        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            tempamount = amount + shipping_amount

        data = {
            'quantuty': c.quantity,
            'amount': amount,
            'totalamount': tempamount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            tempamount = amount + shipping_amount

            data = {
                'quantuty': c.quantity,
                'amount': amount,
                'totalamount': tempamount
            }

        return JsonResponse(data)


def remove_cart(request):
        if request.method == 'GET':
            prod_id = request.GET['prod_id']
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.delete()
            amount = 0.0
            shipping_amount = 70.0
            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                
            data = {
                'amount': amount,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)


def buy_now(request):
    return render(request, 'app/buynow.html')


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add': add, 'active': 'btn-primary'})


def orders(request):
    return render(request, 'app/orders.html')


def change_password(request):
    return render(request, 'app/changepassword.html')


# Mobile Page
def mobile(request, data=None):
    mobile_brand = Product.objects.values_list('brand', flat=True).filter(category='M').distinct()

    if data == None:
        mobiles = Product.objects.filter(category='M')
        print(mobiles)

    elif data != None:
        mobiles = Product.objects.filter(category='M').filter(brand=data)
        print(mobiles)
    return render(request, 'app/mobile.html', {'mobiles': mobiles, 'mobile_brand': mobile_brand})


# Laptop Page
def laptop(request, data=None):
    laptop_brand = Product.objects.values_list('brand', flat=True).filter(category='L').distinct()

    if data == None:
        laptops = Product.objects.filter(category='L')
        print(laptops)

    elif data != None:
        laptops = Product.objects.filter(category='L').filter(brand=data)
        print(laptops)
    return render(request, 'app/laptop.html', {'laptops': laptops, 'laptop_brand': laptop_brand})


# Top-Wear Page
def topwear(request, data=None):
    topwear_brand = Product.objects.values_list('brand', flat=True).filter(category='TW').distinct()

    if data == None:
        topwear = Product.objects.filter(category='TW')
        print(topwear)

    elif data != None:
        topwear = Product.objects.filter(category='TW').filter(brand=data)
        print(topwear)
    return render(request, 'app/topwear.html', {'topwear': topwear, 'topwear_brand': topwear_brand})


# Bottom-Wear Page
def bottomwear(request, data=None):
    bottomwear_brand = Product.objects.values_list('brand', flat=True).filter(category='BW').distinct()

    if data == None:
        bottomwear = Product.objects.filter(category='BW')
        print(bottomwear)

    elif data != None:
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)
        print(bottomwear)
    return render(request, 'app/bottomwear.html', {'bottomwear': bottomwear, 'bottomwear_brand': bottomwear_brand})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationFrom()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registretion successfully")
        return render(request, 'app/customerregistration.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=usr, name=name, locality=locality, city=city, zipcode=zipcode, state=state)
            reg.save()
            messages.success(request, 'Congratulations !! Profile Updated Successfully')

        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})


def checkout(request):
    return render(request, 'app/checkout.html')
