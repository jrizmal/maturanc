from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def iskanje(request):
    if request.user.is_authenticated:
        return render(request,'iskanje/iskanje.html')
    else:
        return redirect('/')

    