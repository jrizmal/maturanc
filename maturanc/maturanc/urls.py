"""maturanc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import domov.views as domov_views
import profil.views as profil_views
import iskanje.views as iskanje_views

urlpatterns = [
    url(r'^profil/urejanje/', profil_views.urediProfil,name='urejanje_profila'),
    url(r'^admin/', admin.site.urls),
    url(r'^profil/', profil_views.profil,name='profil'),
    url(r'^iskanje/', iskanje_views.iskanje,name='iskanje'),
    url(r'^api/', include('api.urls'),name='api'),
    url(r'', domov_views.domov,name='domov'),
]
