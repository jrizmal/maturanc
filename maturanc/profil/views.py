from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profil(request):
    if request.user.is_authenticated:

        profil=request.user.profil
        socialnaomrezja=request.user.socialnaomrezja
        
        return render(request,'profil/profil.html',{'profil':profil,'social':socialnaomrezja})
    else:
        return HttpResponse("You must be logged in to access this page.")
def urediProfil(request):
    return render(request,'profil/urejanje.html')