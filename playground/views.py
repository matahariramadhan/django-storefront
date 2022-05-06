from django.shortcuts import render
from store.models import Product

# Create your views here.
def say_hello(request):
    # filter query using keyword=value (queryset api)
    query_set = Product.objects.filter(unit_price__range=(20,30))

    # # query relation to collection
    # query_set = Product.objects.filter(collection__id__range=(1,2,3))

    # query_set = Product.objects.filter(description__isnull=True)

    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'products': list(query_set)})