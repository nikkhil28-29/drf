from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from products.models import Product
import json

#usi
# @api_view(['POST'])
def api_home(request, *args, **kwargs):
    model_data=Product.objects.all().order_by('?').first() #generate random fields,
    data={}
    if model_data:
        data=model_to_dict(model_data,fields=['id','price']) # i can specify which field that i want api to respond 

    return JsonResponse(data)