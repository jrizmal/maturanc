from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profil(request):
    return render(request,'profil/profil.html')

def urediProfil(request):
    return render(request,'profil/urejanje.html')