from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from models import Sporocilo, Kontakt
from django.db.models import Q

# Create your views here.
def chat(request):
    if request.user.is_authenticated:
        jaz=request.user
        sogovornik=None
        try:
            sogovornik=int(request.GET.get('user',None))
        except:
            pass

        if sogovornik == None:
            kontakti = Kontakt.objects.filter(oseba1=request.user).order_by('-zadnji_stik')
            return render(request,'chat/chat.html',{'kontakti':kontakti})
        else:
            sogovornik_user = User.objects.get(id=sogovornik)
            if Kontakt.objects.filter(Q(oseba1=jaz) & Q(oseba2=sogovornik_user)).exists():
                kontakti = Kontakt.objects.filter(oseba1=jaz).order_by('-zadnji_stik')
                return render(request,'chat/chat.html',{'kontakti':kontakti})
            else:
                Kontakt.objects.create(oseba1=jaz, oseba2=sogovornik_user)
                Kontakt.objects.create(oseba1=sogovornik_user, oseba2=jaz)
                kontakti = Kontakt.objects.filter(oseba1=jaz).order_by('-zadnji_stik')
                return render(request,'chat/chat.html',{'kontakti':kontakti})
    else:
        return redirect('/')