from django.shortcuts import render
from django.db.models import F
from store.models import Product

# Create your views here.
def say_hello(request):
    # # sorting by unit_price dsc AND title asc
    query_set = Product.objects.order_by('unit_price', '-title').reverse()

    # get first object
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')

    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'products': list(query_set)})