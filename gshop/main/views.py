from django.shortcuts import render
from .models import Poster
from product.models import Product


def index(request):
    posters = Poster.objects.all()
    counter = [obj.id - 1 for obj in posters]
    products = Product.objects.all()
    context = {'posters': posters,
               'counter': counter,
               'products': products}
    return render(request, 'main/index.html', context)
