from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from products.models import Products


def home_view(request):
    return redirect('products:list')


def products_list(request):
    products = Products.objects.all()
    context = {"products": products}
    return render(request, 'products.html', context)
