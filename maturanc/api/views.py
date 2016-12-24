from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def prijava(request):
    pUIme=request.GET.get('uIme',None)
    pGeslo=request.GET.get('uGeslo',None)

    uporabnik = authenticate(username=pUIme,password=pGeslo)

    if uporabnik is not None:
        login(request, uporabnik)
        return HttpResponse("prijava uspesna")
    else:
        return HttpResponse("prijava neuspesna")


    return HttpResponse("prijava")

def odjava(request):
    logout(request)
    return HttpResponse("odjava")

def niZahteve(request):
    return HttpResponse("maturanc api v1")