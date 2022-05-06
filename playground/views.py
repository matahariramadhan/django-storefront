from django.shortcuts import render
from django.db.models import Q
from store.models import Product

# Create your views here.
def say_hello(request):
    # products: inventory < 10 AND inventory < 20, this simple query can be done like this:
    # query_set = Product.objects.filter(inventory__lt=10, inventory__lt=20)

    # products: inventory < 10 AND NOT inventory < 20, this complex query can be done like this:
    query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(inventory__lt=20))


    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'products': list(query_set)})