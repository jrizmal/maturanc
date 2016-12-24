from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def iskanje(request):
    return render(request,'iskanje/iskanje.html')