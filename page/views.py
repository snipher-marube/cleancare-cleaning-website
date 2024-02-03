from django.shortcuts import render

def home(request):
    return render(request, 'page/home.html')

def contact(request):
    return render(request, 'page/contact.html')

def about(request):
    return render(request, 'page/about.html')

def pricing(request):
    return render(request, 'page/pricing.html')

def services(request):
    return render(request, 'page/services.html')

def portifolio(request):
    return render(request, 'page/portifolio.html')
