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

def shraniSpremembe(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            """
            bio:Jaka Testni profil.....
            sola:SSKER Celje
            regija:Savinjska
            visina:182
            datum_plesa:Feb. 3, 2017, 6 p.m.
            starost:18
            """
            new_bio = request.POST.get('bio',None)
            new_sola = request.POST.get('sola',None)
            new_regija = request.POST.get('regija',None)
            new_visina = request.POST.get('visina',None)
            new_datum_plesa = request.POST.get('datum_plesa_submit',None)
            new_starost = request.POST.get('starost',None)
            new_spol = request.POST.get('spol',None)
            
            instance = request.user.profil

            instance.sola = new_sola
            instance.regija = new_regija

            if new_spol == "":
                new_spol = None
            else:
                if new_spol == "1":
                    new_spol = True
                elif new_spol == "2":
                    new_spol = False
                else:
                    new_spol = None
            instance.spol = new_spol

            if new_starost == "":
                new_starost = None
            instance.starost = new_starost

            if new_visina == "95":
                new_visina = None
            instance.visina = new_visina

            instance.bio = new_bio
            
            if new_datum_plesa == "":
                new_datum_plesa = None
            instance.datum_plesa = new_datum_plesa
           
            instance.save()
            
        return redirect("/profil/")
    else:
        return redirect('/')