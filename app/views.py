from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Cart, Customer, OrderPlaced, Wishlist, Product
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

import paypalrestsdk
from django.conf import settings

# Create your views here.

def home(request):
    totalitem = 0
    wishitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,"home.html",locals())
def about(request):
    totalitem = 0
    wishitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,"about.html",locals())
def contact(request):
    totalitem = 0
    wishitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,"contact.html",locals())

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"category.html",locals())
        
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"category.html",locals())
    
    
class ProductDetail(LoginRequiredMixin,View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product)&Q(user=request.user))
        
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"productdetail.html",locals())
    
    
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"customerregistration.html",locals())
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
            
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'customerregistration.html',locals())
    
class  ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm() 
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,'profile.html',locals())
    
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            
            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,
                           zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'profile.html',locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,'address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,'updateAddress.html',locals())
        
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Profile Update Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect("address")

def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")
    
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40.00
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    
    return render(request,'addtocart.html',locals())

# Configure PayPal SDK
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # sandbox or live
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

class checkout(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40
        amount = int(totalamount * 100)
        
        return render(request, 'checkout.html', locals())
    
    def post(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": f"{totalamount:.2f}",
                    "currency": "USD"
                },
                "description": "IIUC Hall Management Payment"
            }],
            "redirect_urls": {
                "return_url": request.build_absolute_uri('/execute/'),
                "cancel_url": request.build_absolute_uri('/cancel/')
            }
        })
        
        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    approval_url = link.href
                    break
            return redirect(approval_url)
        else:
            messages.error(request, "Error creating PayPal payment")
            return redirect('checkout')


def execute(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        messages.success(request, "Payment executed successfully")
        return redirect('home')
    else:
        messages.error(request, payment.error)
        return redirect('checkout')

def cancel(request):
    messages.error(request, "Payment canceled")
    return redirect('checkout')



def orders(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request,'orders.html',{'order_placed': order_placed})

# cart...
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_items = Cart.objects.filter(Q(product_id=prod_id) & Q(user=request.user))
        
        cart_item = cart_items.first()
        cart_item.quantity += 1
        cart_item.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 40
        data = {
            'quantity': cart_item.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
    return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_items = Cart.objects.filter(Q(product_id=prod_id) & Q(user=request.user))
        

        cart_item = cart_items.first()
        cart_item.quantity -= 1
        cart_item.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 40
        data = {
            'quantity': cart_item.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
    return JsonResponse(data)




def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        cart_items = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user))
        cart_item = cart_items.first()
        
        
        cart_item.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data = {
            'message': 'Wishlist Added Successfully.',
        }
        return JsonResponse(data)


def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
                'message': 'Wishlist Removed Successfully.',
            }
        return JsonResponse(data)

def search(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    
    search_query = request.GET.get('search', '').strip()
    products = []
    message = ''
    if search_query:
        products = Product.objects.filter(title__icontains=search_query)
        if not products:
            message = 'No products found for "{}"'.format(search_query)
    else:
        message = 'Please enter a search term!'
    
    return render(request, 'search.html', {
        'products': products,
        'search_query': search_query,
        'totalitem': totalitem,
        'wishitem': wishitem,
        'message': message
    })






def wishlist_view(request):
    user = request.user
    wishlist_items = Wishlist.objects.filter(user=user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})
