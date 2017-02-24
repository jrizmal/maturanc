from models import Kontakt

def nova_sporocila(request):
    if request.user.is_authenticated:
        jaz = request.user
        moji_kontakti = Kontakt.objects.filter(oseba1=jaz)
        st_novih_sporocil = 0
        for k in moji_kontakti:
            if k.nova_sporocila:
                st_novih_sporocil=st_novih_sporocil+1

        return {'nova_sporocila':st_novih_sporocil}
    else:
        return {'nova_sporocila':"jaka"}