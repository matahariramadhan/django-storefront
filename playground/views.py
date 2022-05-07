from django.shortcuts import render
from store.models import Product, OrderItem, Order

# Create your views here.
def say_hello(request):
    # select_related for one
    # query_set = Product.objects.select_related('collection').all()

    # pre_fetch for many
    # query_set = Product.objects.prefetch_related('promotion').all()

    # get the last 5 orders with their customer and items (including product)
    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('placed_at')[:5]

    return render(request, "hello.html", {'name': 'Matahari Ramadhan', 'orders': list(query_set)})