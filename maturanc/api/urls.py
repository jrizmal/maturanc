from django.conf.urls import url
import views

urlpatterns = [
    url(r'^odjava/', views.odjava, name='odjava_uporabnika'),
    url(r'^prijava/', views.prijava, name='prijava_uporabnika'),
    url(r'', views.niZahteve, name='ni_zahteve'),
]
