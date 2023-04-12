from django.urls import path
from . import views

urlpatterns = [
    path('', views.cat, name='cat'),
    path('<str:category>/', views.catalog_by_category, name='category'),
    path('<str:category>/<str:brand>', views.catalog_by_brand, name='brand'),
    path('<str:category>/<str:sex>', views.catalog_by_sex, name='sex'),
]
