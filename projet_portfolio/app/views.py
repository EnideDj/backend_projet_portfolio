from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def portfolio(request):
    return render(request, 'app/body/main/portfolio_detail.html')