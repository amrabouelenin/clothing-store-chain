from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Api Overview Endpoint index url
    path('', auth_views.LoginView.as_view(template_name="login.html", extra_context={next:'home'}),name='login'),
    path('home', views.HomePage,name='home'),
    path('reports', views.DailyReports,name='daily_report'),

]