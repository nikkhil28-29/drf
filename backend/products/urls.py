from django.urls import path
from .views import ProductDetailAPIView  # Import the view class
from .models import Product  # Import the User model
from .serializers import ProductSerializer  # Import the UserSerializer

urlpatterns = [
    path('', ProductDetailAPIView.as_view(), name='user-list'),
]