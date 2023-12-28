from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from products.serializers import ProductSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Product


class ProductDetailAPIView(
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ??

product_detail_view = ProductDetailAPIView.as_view()

