from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import *
app_name = CatalogConfig.name
urlpatterns = [
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('catalog/', ProductsListView.as_view(), name='catalog'),
    path('product_items/<int:pk>/', ProductDetailView.as_view(), name='product_items'),
    path('contacts/', never_cache(ContactCreateView.as_view()), name='contacts'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_form'),
    path('product/update_cutted/<int:pk>/', ProductUpdateCuttedView.as_view(), name='product_form_cutted'),
    path('product/create/', never_cache(ProductCreateView.as_view()), name='save_product'),
    path('product/update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_form'),
    path('product/update_cutted/<int:pk>/', never_cache(ProductUpdateCuttedView.as_view()), name='product_form_cutted'),
]
