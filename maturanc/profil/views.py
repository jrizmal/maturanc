from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import ProfilnaSlika
from .forms import ProfilnaSlikaForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from allauth.account.signals import user_signed_up
from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver
from datetime import date
from api.serializers import UserSearchSerializer, ProfilSearchSerializer
from rest_framework.renderers import JSONRenderer
from chat.models import Sporocilo, Kontakt
from django.db.models import Q

# Create your views here.
def profil(request):
    if request.user.is_authenticated:

        profil=request.user.profil
        socialnaomrezja=request.user.socialnaomrezja

        # User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))
        kontakti = Kontakt.objects.filter(Q(oseba1__id=request.user.id) | Q(oseba2__id=request.user.id))

        if request.user.profil.starost is not None:
            starost = calculate_age(request.user.profil.starost)
            return render(request,'profil/profil.html',{'profil':profil,'social':socialnaomrezja,'starost':starost,'kontakti':kontakti})
        else:
            return render(request,'profil/profil.html',{'profil':profil,'social':socialnaomrezja,'kontakti':kontakti})
    else:
        return redirect('/')

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

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
            new_datum_rojstva = request.POST.get('datum_rojstva_submit',None)
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

            if new_datum_rojstva == "":
                new_datum_rojstva = None
            instance.starost = new_datum_rojstva

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

def registracija(request):
    if request.method == 'POST':
        txt_ime = request.POST.get('ime', None)
        txt_priimek = request.POST.get('priimek', None)
        txt_email = request.POST.get('email', None)
        txt_geslo = request.POST.get('geslo', None)

        txt_spol = request.POST.get('spol', None)
        int_spol = int(txt_spol)
        
        spol_bool = False

        if(int_spol==1):
            spol_bool = True
        
        if(int_spol==2):
            spol_bool = False

        

        nov_uporabnik = User.objects.create_user(username=txt_email,email=txt_email,password=txt_geslo, first_name=txt_ime, last_name=txt_priimek)
        nov_uporabnik.profil.spol = spol_bool
        nov_uporabnik.profil.save()

        if nov_uporabnik is not None:
            uporabnik = authenticate(username=txt_email,password=txt_geslo)

            if uporabnik is not None:
                login(request, uporabnik)
                return redirect('/')
            else:
                return HttpResponse("prijava neuspesna")
        else:
            return HttpResponse("uporabnik ni ustvarjen")
    else:
        return redirect('/')

def shraniOmrezja(request):
    if request.method == 'POST':
        new_facebook = request.POST.get('facebook', None)
        new_snapchat = request.POST.get('snapchat', None)
        new_instagram = request.POST.get('instagram', None)
        new_twitter = request.POST.get('twitter', None)

        request.user.socialnaomrezja.facebook = new_facebook
        request.user.socialnaomrezja.snapchat = new_snapchat
        request.user.socialnaomrezja.instagram = new_instagram
        request.user.socialnaomrezja.twitter = new_twitter

        request.user.socialnaomrezja.save()

        return HttpResponse("omrezja shranjena")
    else:
        return redirect('/')
def publicProfil(request, id_uporabnika):
    if request.user.is_authenticated:
        uporabnik = User.objects.get(pk = id_uporabnika)
        profil = uporabnik.profil
        socialnaomrezja = uporabnik.socialnaomrezja
        profilna_slika = uporabnik.profilnaslika
        if profil.starost is not None: 
            starost = calculate_age(profil.starost)
            return render(request,'public_profil/public_profil.html',{'public_user':uporabnik,'public_profil':profil,'public_social':socialnaomrezja,'public_profilna_slika':profilna_slika,'public_starost':starost})
        else:
            return render(request,'public_profil/public_profil.html',{'public_user':uporabnik,'public_profil':profil,'public_social':socialnaomrezja, 'public_profilna_slika':profilna_slika})
    else:
        return redirect('/')