from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import  TransactionSerializer, ServicesCallSerializer
from products.models import  Transaction, Product
from .models import ServicesCall
from rest_framework import permissions, authentication
from rest_framework.permissions import IsAuthenticated
from datetime import date

# Returns list of Transactions
@api_view(['GET'])
def TransactionsList(request):
   
    # get Transactions info
    Transactions = Transaction.objects.all()
    
    # serialize all objects returned
    serializer = TransactionSerializer(Transactions, many=True)

    return Response(serializer.data)

# Returns info of certain Transaction
@api_view(['GET'])
def TransactionDetail(request, pk):
   
    # get Transaction info by id
    Transaction_info = Transaction.objects.get(id=pk)
    
    # serialize Transaction information
    serializer = TransactionSerializer(Transaction_info, many=False)

    return Response(serializer.data)

# API to save new Transaction
@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def AddTransaction(request):
    
    # save json data recieved from post into revenu table
    serializer = TransactionSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
# Returns sum list of today transactions
@api_view(['GET'])
def TransactionsToday(request):
   
    # get Transactions info by created data
    Transactions = Transaction.objects.prefetch_related('product').filter(created=date.today())
    Total_loss = 1500
    Total_reveneu = 0
    prices = []
    for record in Transactions:
        prices.append([record.product.id, record.product.price])
        #product_price = Product.objects.get(id=product_id)
        Total_reveneu += record.amount * record.product.price
    
    #serializer = TransactionSerializer(Transactions, many=True)
    data ={
        "date": date.today(),
        "revenu": Total_reveneu,
        "loses": Total_loss,
        "Branch": 1
    }
    return Response(data)

# add service call
# API to save new Transaction
@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def AddServicesCall(request):
    
    # save json data recieved from post into revenu table
    serializer = ServicesCallSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Returns list of Transactions
@api_view(['GET'])
def ServicesCallsList(request):
   
    # get Transactions info
    ServicesCalls = ServicesCall.objects.all()
    
    # serialize all objects returned
    serializer = ServicesCallSerializer(ServicesCalls, many=True)

    return Response(serializer.data)

# update service calls

@api_view(['POST'])
def ServiceCallUpdate(request, pk):
	servicescall = ServicesCall.objects.get(id=pk)
	serializer = ServicesCallSerializer(instance=servicescall, data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
