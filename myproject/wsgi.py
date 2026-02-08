"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# Tuodaan Pythonin os-kirjasto.
# Tätä tarvitaan, kun asetetaan ympäristömuuttujia (kuten projektin asetukset).
import os

# Tuodaan Djangon get_wsgi_application-funktio.
# Tämä funktio rakentaa WSGI-sovelluksen,
# jota käytetään, kun projektia ajetaan perinteisessä web-palvelimessa
# (esim. Apache tai uWSGI).
from django.core.wsgi import get_wsgi_application

# Asetetaan Djangon asetustiedosto oletusarvoksi.
# Tämä kertoo, mistä Django löytää projektin asetukset (settings.py).
# 'myproject.settings' tarkoittaa: käytä myproject-kansion settings.py-tiedostoa.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Luodaan varsinainen WSGI-sovellus.
# Tämä on se "application"-muuttuja, jonka web-palvelin lataa
# ja jota se käyttää jokaista sivupyyntöä varten.
# Selkokielellä: "Tässä tehdään se sovellus, jota palvelin käyttää
# kun käyttäjä avaa sivun."
application = get_wsgi_application()
