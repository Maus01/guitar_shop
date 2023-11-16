from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from user.models import UserBase

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    image_banner = models.ImageField(upload_to='images/', blank=True, null=True)
    image_index = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'categories' 

    def get_absolute_url(self):
        return reverse('core:category', args=[self.slug])
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    

    def get_absolute_url(self):
        return reverse('core:category_list', args=[self.slug])
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    price = models.IntegerField()
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    on_stock = models.IntegerField(default=5)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    product_code = models.CharField(max_length=120)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + "-" + self.product_code)
        super(Product, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('core:product_detail', args=[self.slug])
    
class Order(models.Model):
    user = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    order_price = models.IntegerField()
    no_of_items = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse("core:order_detail", args=[self.id])
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_price = models.IntegerField()
    total_price = models.IntegerField()

