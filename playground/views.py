from django.shortcuts import render
from django.db.models import F
from store.models import Product, OrderItem

# Create your views here.
def say_hello(request):
    # # value return dictionary, value_list return tupple
    # query_set = Product.objects.values('id', 'title', 'collection__id')

    # select product that have been ordered and sort them by their title
    query_set = Product.objects.filter(
        pk__in=OrderItem.objects.values('product_id').distinct()
        ).order_by('title')

    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'products': list(query_set)})