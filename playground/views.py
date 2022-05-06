from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

# Create your views here.
def say_hello(request):
    # query_set = Product.objects.all() # this return query set

    # try: # need try catch block to catch exception
    #     product = Product.objects.get(pk=0) # this return actual object
    # except ObjectDoesNotExist:
    #     pass

    # query_set = Product.objects.filter(pk=0).first() # better way to do above logic

    isExist = Product.objects.filter(pk=0).exists() # checking if object is exist or not

    return render(request, "hello.html", {'name': 'Matahari Ramadhan'})