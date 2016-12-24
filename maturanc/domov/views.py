from django.shortcuts import render

# Create your views here.
def domov(request):
    return render(request,'domov/domov.html',{"tekst":"jaka"})