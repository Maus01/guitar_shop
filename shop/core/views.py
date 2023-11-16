from django.shortcuts import render, get_object_or_404
from django.contrib.sessions.models import Session
from django.http import HttpResponse

from .models import Category, Product, Brand, Order, OrderItem
from cart.cart import Cart, CartAuth
from .order_history import OrderManager

# context processors

def category_list(request):
    return {'category_list': Category.objects.all()}

#------------------------------------------------------------------



def index(request):
    user = request.user
    best_sellers = Product.objects.all()
    context = {'user':user, 'best_sellers':best_sellers}
    return render(request, 'core/index.html', context)

# Overview of single category with all products
def category(request, slug_category):
    category = get_object_or_404(Category, slug=slug_category)
    products = Product.objects.filter(category=category)
    brands = Brand.objects.all()
    context = {'category':category, 'products':products, 'brands':brands}
    return render(request, 'core/category.html', context)


#Detail of selected product (description, price, availability, pictures....)
def product_detail(request, slug_product):
    product = get_object_or_404(Product, slug=slug_product)
    context = {'product':product}
    
    return render(request, 'core/detail.html', context)


#Final overview of the order.
def checkout(request):
    cart = Cart(request)
    context = {'cart':cart}
    return render(request, 'core/checkout.html', context)


#Finishes the order and saves the order in history if user is signed in
def complete_order(request):
    if request.user.is_authenticated:
        manager = OrderManager(request)
        manager.archive_current_order()
    cart = Cart(request)
    cart.delete_cart()
    if request.user.is_authenticated:
        cart_auth = CartAuth(request)
        cart_auth.delete_cart_auth()
    return render(request,'core/complete_order.html')


#Shows all orders made by user
def history_list(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, 'core/history_list.html', context)


#Details of a single order from history
def order_detail(request, id):
    manager = OrderManager(request)
    items = manager.get_order_detail(id)
    subtotal = manager.get_order_price(id)
    context = {'items':items, 'subtotal':subtotal}
    print(items[0].values())
    return render(request, 'core/order_detail.html', context)
