from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100)
  products = models.ManyToManyField('Product', related_name='categories')
  
  def __str__(self):
    return self.name
  
  
class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=8, decimal_places=2)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  
class Order(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  products = models.ManyToManyField(Product, through='OrderItem')
  total_price = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"Order #{self.pk}"
  
  
class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()
  
  def __str__(self):
    return f"OrderItem #{self.pk} - {self.product.name}"
  