from django.shortcuts import render
from django.views import View
from .models import  Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationFrom
from django.contrib import messages


# Product View in Home Page
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottompwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        return render(request,'app/home.html',{'topwears':topwears,'bottompwears':bottompwears,'mobiles':mobiles,'laptop':laptop,
        })

# Product Details Page
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        # print(product)
        return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

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
    return render(request, 'app/mobile.html', {'mobiles':mobiles,'mobile_brand':mobile_brand})


# Laptop Page
def laptop(request, data=None):
    laptop_brand = Product.objects.values_list('brand', flat=True).filter(category='L').distinct()

    
    if data == None:  
        laptops = Product.objects.filter(category='L')
        print(laptops)
        
    elif data != None:
        laptops = Product.objects.filter(category='L').filter(brand=data)
        print(laptops)
    return render(request, 'app/laptop.html', {'laptops':laptops,'laptop_brand':laptop_brand})


# Top-Wear Page
def topwear(request, data=None):
    topwear_brand = Product.objects.values_list('brand', flat=True).filter(category='TW').distinct()

    
    if data == None:  
        topwear = Product.objects.filter(category='TW')
        print(topwear)
        
    elif data != None:
        topwear = Product.objects.filter(category='TW').filter(brand=data)
        print(topwear)
    return render(request, 'app/topwear.html', {'topwear':topwear,'topwear_brand':topwear_brand})

# Bottom-Wear Page
def bottomwear(request, data=None):
    bottomwear_brand = Product.objects.values_list('brand', flat=True).filter(category='BW').distinct()

    
    if data == None:  
        bottomwear = Product.objects.filter(category='BW')
        print(bottomwear)
        
    elif data != None:
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)
        print(bottomwear)
    return render(request, 'app/bottomwear.html', {'bottomwear':bottomwear,'bottomwear_brand':bottomwear_brand})



def login(request):
 return render(request, 'app/login.html')



class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationFrom()
        return render(request,'app/customerregistration.html',{'form':form})

    def post(self, request):
        form = CustomerRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registretion successfully")
        return render(request,'app/customerregistration.html',{'form':form})
    

def checkout(request):
 return render(request, 'app/checkout.html')
