from django.contrib import admin

# Register your models here.
from models import Sporocilo, Kontakt
# Register your models here.

class KontaktAdmin(admin.ModelAdmin):
    list_display = ('oseba1', 'oseba2', 'nova_sporocila')


admin.site.register(Sporocilo)
admin.site.register(Kontakt, KontaktAdmin)