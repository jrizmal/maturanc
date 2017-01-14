from .models import ProfilnaSlika
from django import forms

class ProfilnaSlikaForm(forms.ModelForm):
    class Meta:
        model = ProfilnaSlika
        fields = ('slika', )