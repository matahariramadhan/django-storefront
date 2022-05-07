from operator import concat
from unittest import result
from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer

# Create your views here.
def say_hello(request):
    queryset = Customer.objects.annotate(
        orders_count=Count('order')
    )
    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'result': queryset})