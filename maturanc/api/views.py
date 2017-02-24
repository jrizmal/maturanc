from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .serializers import UserSearchSerializer, ProfilSearchSerializer, SporociloSerializer
from rest_framework.renderers import JSONRenderer
from profil.models import Profil
from django.contrib.auth.models import User
from chat.models import Sporocilo, Kontakt
from django.db.models import Q
from datetime import datetime

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

def iskanje(request):
    if request.user.is_authenticated:
        vsiUporabniki=request.GET.get('spol',None) #-1 --> vsi
        visina1=request.GET.get('visina1',None)
        visina2=request.GET.get('visina2',None)
        regija = request.GET.get('regija',None)
        sola = request.GET.get('sola',None)

        spol = not request.user.profil.spol
        uporabniki = []
        if vsiUporabniki == '-1':
            uporabniki = User.objects.all().filter(profil__spol=spol)
            serializer = UserSearchSerializer(uporabniki, many=True)
            json = JSONRenderer().render(serializer.data)
            return HttpResponse(json)
        else:
            if sola is not None and sola != "":
                if regija is not None and regija != "":
                    uporabniki = User.objects.all().filter(profil__visina__gte=visina1,profil__visina__lte=visina2,profil__spol=spol, profil__sola__iexact=sola, profil__regija__iexact=regija)
                else:
                    uporabniki = User.objects.all().filter(profil__visina__gte=visina1,profil__visina__lte=visina2,profil__spol=spol, profil__sola__iexact=sola)
            else:
                if regija is not None and regija != "":
                    uporabniki = User.objects.all().filter(profil__visina__gte=visina1,profil__visina__lte=visina2,profil__spol=spol, profil__regija__iexact=regija)
                else:
                    uporabniki = User.objects.all().filter(profil__visina__gte=visina1,profil__visina__lte=visina2,profil__spol=spol)
            # MyClass.objects.filter(name__iexact=my_parameter)
            serializer = UserSearchSerializer(uporabniki, many=True)
            json = JSONRenderer().render(serializer.data)
            return HttpResponse(json)
        """
        if spolIndexInt == 1:
            spol = True
            uporabniki = User.objects.all().filter(profil__visina__gte=visina1,profil__visina__lte=visina2,profil__spol=spol)
        if spolIndexInt == 2:
            spol=False
            uporabniki = User.objects.all().filter(profil__visina__gte=visina1,profil__visina__lte=visina2,profil__spol=spol)
        if spolIndexInt == -1:
            uporabniki = User.objects.all()
        
        serializer = UserSearchSerializer(uporabniki, many=True)

        json = JSONRenderer().render(serializer.data)

        

        return HttpResponse(json)
        """
    else:
        return HttpResponse("niste prijavljeni")
    """
    spol: spolIndex,
    visina1: visina[0],
    visina2: visina[1],
    """
    
def uporabnikObstaja(request):
    txt_email = request.GET.get('email',None)
    if User.objects.filter(email=txt_email).exists() == True:
        return HttpResponse('""')
    else:
        return HttpResponse('"true"')

def dobiSporocila(request):
    try:
        seen = request.GET.get('seen',None)
        samo_nova = request.GET.get('samo_nova',None)
        starejsa = request.GET.get('starejsa',None)
        timestamp = request.GET.get('timestamp',None)
        id_user_1 = int(request.GET.get('oseba1', None))
        id_user_2 = int(request.GET.get('oseba2', None))
    except:
        return HttpResponse('"napaka v parametrih"')
    if seen == 'da':
        temp = Kontakt.objects.get(oseba1__id=id_user_1, oseba2__id=id_user_2)
        temp.zadnji_stik = datetime.now()
        temp.nova_sporocila = False
        temp.save()
    
    if samo_nova == 'da':
        sporocila = Sporocilo.objects.filter((Q(posiljatelj__id = id_user_1) | Q(posiljatelj__id = id_user_2)) & (Q(prejemnik__id = id_user_1) | Q(prejemnik__id = id_user_2)) & Q(cas_posiljanja__gt=timestamp)).order_by('cas_posiljanja')
        serializer = SporociloSerializer(sporocila, many=True)
        json = JSONRenderer().render(serializer.data)
        return HttpResponse(json)
    else:
        if starejsa == 'da':
            sporocila = Sporocilo.objects.filter((Q(posiljatelj__id = id_user_1) | Q(posiljatelj__id = id_user_2)) & (Q(prejemnik__id = id_user_1) | Q(prejemnik__id = id_user_2)) & Q(cas_posiljanja__lt=timestamp)).order_by('-cas_posiljanja')[:10]
            serializer = SporociloSerializer(sporocila, many=True)
            json = JSONRenderer().render(serializer.data)
            return HttpResponse(json)
        else:
            if id_user_1 == id_user_2:
                vsa_sporocila = Sporocilo.objects.filter(Q(posiljatelj__id = id_user_1) & Q(prejemnik__id = id_user_1)).order_by('-cas_posiljanja')
                # vsa_sporocila = Sporocilo.objects.all()
                serializer = SporociloSerializer(vsa_sporocila, many=True)
                json = JSONRenderer().render(serializer.data)
                return HttpResponse(json)
            else:
                vsa_sporocila = Sporocilo.objects.filter((Q(posiljatelj__id = id_user_1) | Q(posiljatelj__id = id_user_2)) & (Q(prejemnik__id = id_user_1) | Q(prejemnik__id = id_user_2))).order_by('-cas_posiljanja')[:10]
                # vsa_sporocila = Sporocilo.objects.all()
                serializer = SporociloSerializer(vsa_sporocila, many=True)
                json = JSONRenderer().render(serializer.data)
                return HttpResponse(json)

def posljiSporocilo(request):
    if request.method == 'POST':
        try:
            id_posiljatelj = int(request.POST.get('posiljatelj', None))
            id_prejemnik = int(request.POST.get('prejemnik', None))
            msg_besedilo = request.POST.get('besedilo', None)
            try:
                user_posiljatelj = User.objects.get(id = id_posiljatelj)
                user_prejemnik = User.objects.get(id = id_prejemnik)
                if msg_besedilo.strip() != "":
                    Sporocilo.objects.create(posiljatelj = user_posiljatelj, prejemnik = user_prejemnik, besedilo=msg_besedilo)

                    temp = Kontakt.objects.get(oseba1__id=id_prejemnik, oseba2__id=id_posiljatelj)
                    temp.nova_sporocila = True
                    temp.save()
                else:
                    return HttpResponse('"prazen_tekst"')
            except:
                return HttpResponse('"database_error"')
            
            return HttpResponse('"uspesno"')
        except:
            return HttpResponse('"napaka"')
    else:
        return HttpResponse('"send message api"')
        
