from django.db import models

from user.models import UserBase
from core.models import Product


#Cart is stored in databse for loged in user
class CartModel(models.Model):
    user = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    
class CartItem(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    
