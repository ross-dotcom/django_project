from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def home(request):
  return render (request, 'home.html')

def product_list(request):
  products = Product.objects.all()
  return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
  product = Product.objects.get(pk=product_id)
  return render(request, 'product_detail.html', {'product': product})

def category_list(request):
  categories = Category.objects.all()
  return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, category_id):
  category = Category.objects.get(pk=category_id)
  products = category.product_set.all()
  return render(request, 'category_detail.html', {'category': category, 'products': products})