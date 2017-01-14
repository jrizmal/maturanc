from django.shortcuts import render
from profil.models import ProfilnaSlika

# Create your views here.
def domov(request):
    if request.user.is_authenticated:
        profilnaSlika = request.user.profilnaslika.slika
    else:
        profilnaSlika = ""
    return render(request,'domov/domov.html',{"avatar":profilnaSlika})

