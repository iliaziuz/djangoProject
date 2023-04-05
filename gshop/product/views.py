from django.views.generic import DetailView
from .models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_view.html'
    context_object_name = 'product'

