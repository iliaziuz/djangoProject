from django.views.generic import DetailView
from .models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_view.html'
    context_object_name = 'product'

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        images = product.images.all()
        context['images'] = images
        return context'''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        images = product.images.all()
        characteristics = product.characteristics
        context['images'] = images
        context['characteristics'] = characteristics
        return context
