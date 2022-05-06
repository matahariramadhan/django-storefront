from django.shortcuts import render
from django.db.models import F
from store.models import Product

# Create your views here.
def say_hello(request):
    # products: inventory = collection__id
    query_set = Product.objects.filter(inventory=F('collection_id'))

    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'products': list(query_set)})