from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.forms.models import model_to_dict
import json
from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.

@api_view(["GET","POST"])
def api_home(request,*args,**kwargs):
    """
    DRF api view
    """
    # instance= Product.objects.all().order_by("?").first()
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
    return Response(serializer.data)