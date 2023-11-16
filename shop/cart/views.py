from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from core.models import Product
from .cart import Cart, CartAuth

# context processors
def cart(request):
    cart = Cart(request)
    return {'cart':cart}
#------------------------------------------
    
#Add selected product in session and also in database, if user is logged in. 
#Product needs to be added in session in both cases, because cart template loads data from session 
def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_code = request.POST.get('code')
        quantity = int(request.POST.get('quantity'))
        cart.cart_add_product(code=product_code, quantity=quantity)
        no_of_products = str(cart.__len__())
        response = JsonResponse({'no_of_products':no_of_products, "success":True})
        if request.user.is_authenticated:
            cart_auth = CartAuth(request)
            cart_auth.cart_auth_add(code=product_code, quantity=quantity)
       
        return response
 
 
#Overview of all products in cart    
def cart_summary(request):
    cart = Cart(request)
    subtotal = cart.cart_subtotal()
    context = {'subtotal':subtotal}
    return render(request, 'cart/cart.html', context)


#Updates cart if quantity of a product is changed
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_code = request.POST.get('productcode')
        quantity = int(request.POST.get('productqty'))
        cart.update_item(code=product_code, quantity=quantity)
        new_item_price = cart.get_item_price(code=product_code)
        subtotal = cart.cart_subtotal()
        if request.user.is_authenticated:
            cart_auth = CartAuth(request)
            cart_auth.cart_auth_update(code=product_code, quantity=quantity)
        no_of_products = str(cart.__len__())
        response = JsonResponse({'item_total':new_item_price, 'subtotal':subtotal, 'no_of_products':no_of_products, "success":True})
        return response

#Updates cart if a product is deleted    
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_code = request.POST.get('productcode')
        cart.delete_item(product_code)
        subtotal = cart.cart_subtotal()
        no_of_products = str(cart.__len__())
        if request.user.is_authenticated:
            cart_auth = CartAuth(request)
            cart_auth.cart_auth_delete(product_code)
        response = JsonResponse({'subtotal':subtotal, 'no_of_products':no_of_products, "success":True})
        return response
        
        
    
    

    
