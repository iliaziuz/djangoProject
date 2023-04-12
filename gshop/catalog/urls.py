from django.urls import path
from . import views

urlpatterns = [
    path('<str:category>/', views.catalog_by_category, name='category'),
    path('filter/<str:filter_str>/', views.catalog_by_category, name='filter'),
    path('filter/', views.catalog_by_category, name='filter'),

]
