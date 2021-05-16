from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import DailyRevneuSerializer, BranchSerializer
from .models import DailyRevenue, Branch
from rest_framework import permissions, authentication
from rest_framework.permissions import IsAuthenticated

# Overview of the api server urls
@api_view(['GET'])
def ApiOverview(request):

    # list of urls available in the Headquarter Api server
    api_urls = {

        'Branch APIs': {

            'Add Branch': 'api/add/branch/',
            'Update Branch': 'api/update/branch/<int:id>/',
            'Delete Branch': 'api/delete/branch/<int:id>/',
            'Branch Detail': 'api/branch-detail/<int:id>/',
            'List Branches': 'api/branches/',

        },

        'Daily Revneue APIs': {

            'Send Revenue': 'api/send-revenue/',
            'List Revenues': 'api/list/revenue/',

        }
            
    }

    return Response(api_urls)

# Returns list of branches
@api_view(['GET'])
def BranchesList(request):
   
    # get branches info
    branches = Branch.objects.all()
    
    # serialize all objects returned
    serializer = BranchSerializer(branches, many=True)

    return Response(serializer.data)

# Returns info of certain branch
@api_view(['GET'])
def BranchDetail(request, pk):
   
    # get branch info by id
    branche_info = Branch.objects.get(id=pk)
    
    # serialize branch information
    serializer = BranchSerializer(branche_info, many=False)

    return Response(serializer.data)


############################# Revenue Web Service Apis ###################################

# Branch service call to send it's daily revnu and loses
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def SendRevenue(request):
    
    # save json data recieved from post into revenu table
    serializer = DailyRevneuSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Return revenue history
@api_view(['GET'])
#@permission_classes((IsAuthenticated, ))
#@authentication_classes(authentication.TokenAuthentication,)
def RevenueList(request):
    
    revenue_list = DailyRevenue.objects.all()
    serializer = DailyRevneuSerializer(revenue_list, many=True)

    return Response(serializer.data)

