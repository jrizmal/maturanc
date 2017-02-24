from django.conf.urls import url
import views

urlpatterns = [
    url(r'^odjava/$', views.odjava, name='odjava_uporabnika'),
    url(r'^prijava/obstaja/$', views.uporabnikObstaja, name='uporabnik_obstaja'),
    url(r'^prijava/$', views.prijava, name='prijava_uporabnika'),
    url(r'^iskanje/$', views.iskanje, name='iskanje_po_parametrih'),
    url(r'^chat/vsasporocila/$', views.dobiSporocila, name='dobi_sporocila'),
    url(r'^chat/sporocilo/poslji/$', views.posljiSporocilo, name='poslji_sporocilo'),
    url(r'', views.niZahteve, name='ni_zahteve'),
]
