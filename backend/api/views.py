from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from products.models import Product
import json 
from rest_framework import status 
from products.serializers import ProductSerializer


# @api_view(['GET']) #will only respond to HTTP POST requests(not GET,DELETE,UPDATE)
@renderer_classes([JSONRenderer])  # Use only JSONRenderer, not the browsable API renderer

@api_view(['POST','GET'])
def api_home(request):
    if request.method == 'POST':
       # Handle POST request to create a new instance
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        # Handle GET request to retrieve data
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
