from django.urls import path
from.import views
# from rest_framework.authtoken import views as auth_view

urlpatterns=[
    # path('users', views.UserRegisterEndpoint.as_view(), name='users'),
    # path('login', auth_view.ObtainAuthToken.as_view(), name='login-user'),
    path('category', views.CategoryEndpoint.as_view(), name='category'),
    path('category/<int:pk>', views.SingleCategoryEndPoint.as_view(), name="category-up"),
    path('category/<int:pk>/delete', views.CategoryDeleteEndpoint.as_view(), name="category-del"),
    path('category/<int:pk>/update', views.CategoryUpdateEndpoint.as_view(), name="category-up"),
    path('products/<int:pk>', views.SingleProductEndPoint.as_view(), name='products-up'),
    path('products/<int:pk>/delete', views.ProductDeleteEndpoint.as_view(), name='products-del'),
    path('products/<int:pk>/update', views.ProductUpdateEndpoint.as_view(), name='products-up'),
    path('products', views.ProductEndpoint.as_view(), name='products'),
    path('products-list', views.ProductListEndPoint.as_view(), name="products-list"),
    path('products/<int:product_id>', views.ProductDetailEndpoint.as_view(), name='products_id')
]