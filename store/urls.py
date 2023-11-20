from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<str:cat>', views.category, name='category'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('update-wishlist/', views.updateWishlist, name='update-wishlist'),
    path('cart/', views.cart, name='cart'),
    path('update-item/', views.updateItem, name='update-item'),
    path('checkout/', views.checkout, name='checkout'),
    path('process-order/', views.processOrder, name='process-order'),

    path('test/', views.testing, name='store'),
]
