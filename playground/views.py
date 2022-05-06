from django.shortcuts import render
from django.db.models import F
from store.models import Product

# Create your views here.
def say_hello(request):
    # limit result to 5 early object
    query_set = Product.objects.all()[:5]

    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'products': list(query_set)})