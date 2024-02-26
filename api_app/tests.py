from django.urls import path
from.import views

urlpatterns=[
    path('category', views.CategoryEndpoint.as_view(), name='category'),
    path('products', views.ProductEndpoint.as_view(), name='products'),
    path('product/<int:product_id>', views.ProductDetailEndpoint.as_view(), name='products_id')
]