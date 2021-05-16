from django.shortcuts import render



# Create your views here.
# defing login html page
def LoginPage(request):
    return render(request, 'login.html')

def HomePage(request):
    # redirect to home page 
    return render(request, 'home.html', context={})

def DailyReports(request):

    # redirect to products page
    return render(request, 'reports.html', context={})


