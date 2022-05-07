from unittest import result
from django.shortcuts import render
from django.db.models import Value, F
from store.models import Product, OrderItem, Order, Customer

# Create your views here.
def say_hello(request):
    queryset = Customer.objects.annotate(new_id=F('id')+1)
    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'result': queryset})