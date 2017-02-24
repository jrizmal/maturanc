from django.shortcuts import render
from profil.models import ProfilnaSlika

# Create your views here.
def domov(request):
    return render(request,'domov/domov.html')
    

