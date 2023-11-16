from core.views import Product
from .models import CartModel, CartItem
from core.models import Product

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from http import HTTPStatus

#Class for cart stored in session
class Cart:
    def __init__(self, request):
        self.session = request.session
        self.user = request.user
        if 'cart' in self.session:
            cart = self.session['cart']
        else:
            cart = self.session['cart'] = {}
        self.cart = cart
        self.request = request
        
            
            
    def cart_add_product(self, code, quantity):
        if code in self.cart.keys():
            item = self.cart[code]
            item['quantity'] += quantity
        else:
            self.cart[code] = {'quantity':quantity}
        self.save()
            
        return self.cart[code]
    
    #Returns number of products in cart
    def __len__(self):
        keys = self.cart.keys()
        return len(keys)
    
    def save(self):
        self.session.modified = True
     
    #Returns product codes of all items in cart    
    def get_product_codes(self):
        return self.cart.keys()
    
    #Returns quantity of a single product in cart
    def get_item_quantity(self, code):
        product = self.cart[code]
        return product['quantity']
    
    #Returns total price of the cart
    def cart_subtotal(self):
        total_price = []
        keys = self.cart.keys()
        for key in keys:
            item = self.cart[key]
            quantity = item['quantity']
            product = Product.objects.get(product_code=key)
            price = quantity * product.price
            total_price.append(price) 
        return sum(total_price) 
    
    #Updates quantity of a item, if it's changed in the cart
    def update_item(self, code, quantity):
        self.cart[code] = {'quantity':quantity}
        self.save()
    
    #Returns total price of a item        
    def get_item_price(self, code):
        product = Product.objects.get(product_code=code)
        price = product.price
        cart_item = self.cart[code]
        quantity = cart_item['quantity']
        return price * quantity
    
    def delete_item(self, code):
        if code in self.cart:
            del self.cart[code]
            self.save()
       
        
    def __iter__(self):
        codes = self.get_product_codes()
        for code in codes:
            item = {}
            product = get_object_or_404(Product, product_code=code)
            item['product'] = product
            item['item_sum_price'] = product.price * self.cart[code]['quantity']
            item['quantity'] = self.cart[code]['quantity']
            yield item
    
    #If user logs in and has already cart in databse, session is cleared and filled with items from databse        
    def cart_load_from_db(self):
        if CartModel.objects.filter(user=self.user):
            self.delete_cart()
            cart = CartModel.objects.get(user=self.user)
            items = CartItem.objects.filter(cart=cart)
            for item in items:
                self.cart[item.product.product_code] = {'quantity': item.quantity}
                self.save()
                
    def delete_cart(self):
        self.cart.clear()
        self.save()
        
#Class for cart stored in database           
class CartAuth:
    def __init__(self, request):
        self.request = request
        self.user = request.user
        if CartModel.objects.filter(user=self.user).first():
            self.cart_user = CartModel.objects.get(user=self.user)
        else:
            new_cart = CartModel.objects.create(user=self.user)
            new_cart.save()
            self.cart_user = new_cart
            
    #Adds selected product to the cart        
    def cart_auth_add(self, code, quantity):
        product = Product.objects.get(product_code=code)
        if CartItem.objects.filter(product=product, cart=self.cart_user):
            item = CartItem.objects.get(product=product, cart=self.cart_user)
            item.quantity += quantity
            item.save()
        else:
            new_item = CartItem.objects.create(product=product, quantity=quantity, cart=self.cart_user)
            new_item.save()
            return new_item
        
    #Deletes selected product from cart
    def cart_auth_delete(self, code):
        product = Product.objects.get(product_code=code)
        if CartItem.objects.filter(product=product, cart=self.cart_user):
            item = CartItem.objects.get(product=product, cart=self.cart_user)
            item.delete()
            
    #Updates quantity of a product, if it's changed in cart        
    def cart_auth_update(self, code, quantity):
        product = get_object_or_404(Product, product_code = code)
        item = get_object_or_404(CartItem, cart=self.cart_user, product=product)
        item.quantity = quantity
        item.save()
        return item
    
    #Deletes the whole cart
    def delete_cart_auth(self):
        self.cart_user.delete()
        
        
     
        
       
                 
        
        