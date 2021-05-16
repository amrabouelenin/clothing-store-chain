from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes, renderer_classes
from rest_framework.response import Response
from .serializers import ProductSerializer, TransactionSerializer
from products.models import Product, Transaction
from rest_framework import permissions, authentication
from rest_framework.permissions import IsAuthenticated
from .transactionviews import *
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework.views import APIView
#from userprofile.models import User # new

# Overview of the api server urls
@api_view(['GET'])
def ApiOverview(request):

    # list of urls available in the Headquarter Api server
    api_urls = {

        'Product APIs': {

            'Add Product': 'api/add/product/',
            'List Products': 'api/list/products/',

        },
        'Transaction APIs': {

            'Add Transaction': 'api/add/transaction/',
            'List Transactions': 'api/list/transactions/',

        }
            
    }

    return Response(api_urls)

# Returns list of products
@api_view(['GET'])
def ProductsList(request):
   
    # get Products info
    Products = Product.objects.all()
    
    # serialize all objects returned
    serializer = ProductSerializer(Products, many=True)

    return Response(serializer.data)

# Returns info of certain Product
@api_view(['GET'])
def ProductDetail(request, pk):
   
    # get Product info by id
    Product_info = Product.objects.get(id=pk)
    
    # serialize Product information
    serializer = ProductSerializer(Product_info, many=False)

    return Response(serializer.data)

# API to save new product
@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def AddProduct(request):
    
    # save json data recieved from post into revenu table
    serializer = ProductSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class LoginAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'branch-login.html'
    def post(self, request):
        
        user = LoginSerializer(data = request.data)
        if user.is_valid():
            return Response(user.data, status = status.HTTP_200_OK)
        return Response(user.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def simple_html_view(request):
    renderer_classes = [StaticHTMLRenderer]
    data = '<html><body><h1>Hello, world</h1></body></html>'
    return Response(data)

