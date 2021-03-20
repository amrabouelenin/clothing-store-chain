from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Overview of the api server urls
@api_view(['GET'])
def ApiOverview(request):

    # list of urls available in the Headquarter Api server

    api_urls = {
        'Add Branch': 'api/add/branch/',
        'Update Branch': 'api/update/branch/<int:id>/',
        'Delete Branch': 'api/delete/branch/<int:id>/',
        'Branch Detail': 'api/branch-detail/<int:id>/',
        'List Branches': 'api/branches/',
    }

    return Response(api_urls)
