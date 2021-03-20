from django.urls import path
from . import views

urlpatterns = [

    # Api Overview Endpoint index url
    path('', views.ApiOverview, name='api-overview'),
    
    ## Branches urls
    path('branches/', views.BranchesList, name='branch-list'),
    path('branch-detail/<str:pk>/', views.BranchDetail, name='branch-detail'),
    
    ## Daily revenue urls
    path('send-revenue/', views.SendRevenue, name='send-revenue'),
    path('list/revenue/', views.RevenueList, name='revenue-list'),

]