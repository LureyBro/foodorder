from django.shortcuts import render
from demo_app.models import *

# Create your views here.

def homepage(request):
	products=Product.objects.all().order_by('-id')[:8]
	context={
		'products':products
	}
	return render(request,'client/homepage.html',context)

def products(request):
	products=Product.objects.all().order_by('-id')
	context={
		'procucts':products
	}
	return render(request,'client/products.html',context)

def product_details(request,product_id):
	product=Product.objects.get(id=product_id)
	context={
		'product':product
	}
	return render(request,'client/productdetails.html',context)