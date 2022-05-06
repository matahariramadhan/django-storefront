from django.shortcuts import render
from django.db.models import F
from store.models import Product, OrderItem

# Create your views here.
def say_hello(request):
    # becareful using only and defer can cause performance issue
    # below is example of performance issue
    # query_set = Product.objects.only('title')
    query_set = Product.objects.defer('unit_price')

    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'products': list(query_set)})