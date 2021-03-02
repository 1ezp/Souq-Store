from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def product_list(request):
    product_list = Product.objects.get_queryset().order_by('id')
    paginator = Paginator(product_list, 3)

    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    context = {'product_list':product_list}
    return render(request,'Product/product_list.html', context)

def product_detail(request,id):
    product_detail = Product.objects.get(id=id)
    context = {'product_detail':product_detail}
    return render(request,'Product/product_detail.html', context)