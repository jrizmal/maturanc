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
from allauth.account.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
import profil

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
	url(r'^profil/urejanje/$', profil_views.urediProfil,name='urejanje_profila'),
    url(r'^admin/', admin.site.urls),
    url(r'^profil/$', profil_views.profil,name='profil'),
    url(r'^iskanje/$', iskanje_views.iskanje,name='iskanje'),
    url(r'^api/', include('api.urls'),name='api'),
    url(r'^accounts/login/$', LoginView,name='socialLogin'),
    
    url(r'^$', domov_views.domov,name='domov'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
