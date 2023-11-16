from cart.models import CartModel, CartItem
from .models import Order, OrderItem

from django.shortcuts import get_object_or_404

#Class, that hadles history of orders
class OrderManager():
    def __init__(self, request):
        self.request = request
        self.user = request.user
        if CartModel.objects.filter(user=self.user):
            self.cart = CartModel.objects.get(user=self.user)
            
    #Saves the whole cart in history   
    def archive_current_order(self):
        items = CartItem.objects.filter(cart=self.cart)
        cart_price = self.get_cart_price()
        new_order = Order.objects.create(user=self.user, order_price=cart_price, no_of_items=items.count())
        new_order.save()
        for item in items:
            total_price = item.quantity*item.product.price
            quantity = item.quantity
            item_price = item.product.price
            product = item.product
            new_item = OrderItem.objects.create(order=new_order, item_price=item_price, total_price=total_price, quantity=quantity, product=product)
            new_item.save()
    
    #Returns price of the whole order
    def get_cart_price(self):
        items = CartItem.objects.filter(cart=self.cart)
        price = sum([item.quantity*item.product.price for item in items])
        return price
    #Shows complete order saved in history
    def get_order_detail(self, id):
        items = []
        order = get_object_or_404(Order, id=id)
        order_items = OrderItem.objects.filter(order=order)
        for order_item in order_items:
            item = {}
            item['product'] = order_item.product
            item['item_sum_price'] = order_item.item_price
            item['quantity'] = order_item.quantity
            items.append(item)
        return items
    #Returns price of a order saved in database
    def get_order_price(self, id):
        order = get_object_or_404(Order, id=id)
        return order.order_price
            
        