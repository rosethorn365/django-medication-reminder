"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# Tuodaan käyttöön Pythonin os-kirjasto.
# Tätä tarvitaan ympäristömuuttujien (kuten projektin asetusten) lukemiseen.
import os

# Tuodaan Djangosta funktio get_asgi_application.
# Tämä funktio tekee ASGI-sovelluksen, jota palvelin käyttää
# (esim. kun sivu ladataan tai kun WebSocket-yhteys tehdään).
from django.core.asgi import get_asgi_application

# Asetetaan Djangon asetustiedosto projektin oletusasetukseksi.
# Tämä kertoo, mistä Django löytää asetukset (esim. tietokanta, sovellukset, kieli).
# 'myproject.settings' tarkoittaa, että käytetään myproject-kansion settings.py-tiedostoa.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Luodaan varsinainen ASGI-sovellus.
# Tämä muuttuja "application" on se, jota palvelin käyttää
# jokaisen saapuvan pyynnön käsittelyyn.
# Selkokielellä: "Tässä tehdään sovellus, jota palvelin käyttää,
# jotta käyttäjä voi avata sivuja ja käyttää sovellusta."
application = get_asgi_application()
``
