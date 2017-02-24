from rest_framework import serializers
from profil.models import Profil, ProfilnaSlika
from django.contrib.auth.models import User
from chat.models import Sporocilo
from datetime import date

class ProfilnaSlikaSearchSerializer(serializers.ModelSerializer):

    slika_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = ProfilnaSlika
        fields = ('slika_url',)

    def get_image_url(self, obj):
        return obj.slika.url

    

class ProfilSearchSerializer(serializers.ModelSerializer):
    
    starost_leta = serializers.SerializerMethodField('izracunaj_starost')

    class Meta:
        model = Profil
        fields = ('spol', 'visina', 'sola', 'starost','starost_leta')

    def izracunaj_starost(self, obj):
        if obj.starost is not None:
            born = obj.starost
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        else:
            return None

class UserSearchSerializer(serializers.ModelSerializer):

    profil = ProfilSearchSerializer()
    profilnaslika = ProfilnaSlikaSearchSerializer()

    class Meta:
        model = User
        fields = ('pk','username', 'email', 'first_name', 'last_name','profil','profilnaslika')

class SporociloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sporocilo
        fields = ('posiljatelj','prejemnik','besedilo','cas_posiljanja')