from django.urls import path
from . import views

urlpatterns = [

    # Api Overview Endpoint index url
    path('', views.ApiOverview, name='api-overview'),
    
    ## Product urls
    path('list/products/', views.ProductsList, name='products-list'),
    path('product-detail/<str:pk>/', views.ProductDetail, name='product-detail'),
    path('add/product/', views.AddProduct, name='add-product'),
    
    ## Transaction urls
    path('list/transactions/', views.TransactionsList, name='transactions-list'),
    path('transaction-detail/<str:pk>/', views.TransactionDetail, name='transaction-detail'),
    path('transactions_today', views.TransactionsToday, name='transactions-today'),
    path('add/transaction/', views.AddTransaction, name='add-transaction'),

    ## services call
    path('add/servicecall', views.AddServicesCall, name='add-servicecall'),
    path('list/servicescalls/', views.ServicesCallsList, name='servicescalls-list'),
    path('servicecall-update/<str:pk>/', views.ServiceCallUpdate, name="servicecall-update"),
    ## Web client urls
    path('branch-login/', views.simple_html_view, name='branch-login'),
]