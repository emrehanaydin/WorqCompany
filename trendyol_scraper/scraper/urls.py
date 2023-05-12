from django.urls import path
from .views import ProductAPIView

urlpatterns = [
    path('scrap/product', ProductAPIView.as_view(), name='product-scrap'),
]
