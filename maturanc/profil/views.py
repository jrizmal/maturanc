from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import ProfilnaSlika
from .forms import ProfilnaSlikaForm

# Create your views here.
def profil(request):
    if request.user.is_authenticated:

        profil=request.user.profil
        socialnaomrezja=request.user.socialnaomrezja
        
        
        return render(request,'profil/profil.html',{'profil':profil,'social':socialnaomrezja})
    else:
        return redirect('/')


def urediProfil(request):
    if request.user.is_authenticated:
        instance = request.user.profilnaslika
        if request.method == 'POST':
            form = ProfilnaSlikaForm(request.POST, request.FILES, instance = instance)
            if form.is_valid():
                form.save()
                return render(request, 'profil/urejanje.html',{'form': form})
        else:
            form = ProfilnaSlikaForm()
        return render(request, 'profil/urejanje.html', {'form': form})
    else:
        return redirect('/')