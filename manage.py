#!/usr/bin/env python
# Tämä rivi kertoo käyttöjärjestelmälle: "aja tämä tiedosto Pythonilla".
# Se auttaa erityisesti Linux/Mac-ympäristöissä, kun tiedosto ajetaan suoraan.

"""Django's command-line utility for administrative tasks."""
# Tämä on tiedoston kuvaus (docstring).
# Se kertoo lyhyesti, että tämä tiedosto on Djangon komentorivityökalu hallinnollisiin tehtäviin.

import os
# Tuodaan os-kirjasto, jolla voidaan käsitellä käyttöjärjestelmän asetuksia,
# kuten ympäristömuuttujia (environment variables).

import sys
# Tuodaan sys-kirjasto, jolla saadaan käyttöön komentorivin argumentit (sys.argv),
# eli mitä käyttäjä kirjoitti komentoriville (esim. runserver, migrate, createsuperuser).


def main():
    """Run administrative tasks."""
    # Tämä funktio on ohjelman "päätoiminto".
    # Kun manage.py ajetaan, tämä funktio hoitaa Djangon komentojen käynnistyksen.

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    # Asetetaan ympäristömuuttuja DJANGO_SETTINGS_MODULE, jos sitä ei ole jo asetettu.
    # Tämä kertoo Djangolle, mistä se löytää projektin asetukset (settings.py).
    # 'myproject.settings' tarkoittaa: myproject-kansion settings.py.

    try:
        # Yritetään tuoda Djangosta toiminto execute_from_command_line,
        # joka osaa lukea komentoriviltä annetun käskyn ja suorittaa sen.
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        # Jos Djangoa ei löydy (ei asennettu tai virtuaaliympäristö ei ole päällä),
        # päädytään tänne.

        raise ImportError(
            # Tässä annetaan selkeä virheilmoitus käyttäjälle.
            # Viesti kysyy: onko Django asennettu ja onko virtuaaliympäristö aktivoitu.
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        # "from exc" tarkoittaa: liitetään alkuperäinen virhe mukaan,
        # jotta vian etsintä on helpompaa.

    execute_from_command_line(sys.argv)
    # Tämä suorittaa komentoriviltä annetun Djangon komennon.
    # sys.argv sisältää kaikki komentorivin sanat.
    # Esimerkkejä:
    # - python manage.py runserver  -> käynnistää kehityspalvelimen
    # - python manage.py migrate    -> ajaa tietokantamuutokset
    # - python manage.py makemigrations -> luo muutokset malleista


if __name__ == '__main__':
    # Tämä tarkistaa: onko tämä tiedosto käynnistetty suoraan (ei importattuna).
    # Jos ajetaan suoraan, silloin tämä ehto on tosi.

    main()
    # Jos ehto toteutui, kutsutaan main()-funktiota eli käynnistetään toiminta.
