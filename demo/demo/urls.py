# Tuodaan Djangosta käyttöön "path"-toiminto.
# "path" auttaa määrittämään, mitkä verkkosivun osoitteet (URLit) tekevät mitäkin.
from django.urls import path

# Tuodaan tämän sovelluksen (saman kansion) views.py-tiedostosta kaksi toimintoa:
# 1) reminders = näyttää (ja/tai käsittelee) lääkemuistutukset
# 2) reminder_delete = poistaa yhden tietyn lääkemuistutuksen
from .views import reminders, reminder_delete

# Tehdään lista nimeltä urlpatterns.
# Tämä lista kertoo Djangolle, mitä tapahtuu kun käyttäjä menee tiettyyn osoitteeseen.
urlpatterns = [

    # Reitti: "reminders/"
    # Kun käyttäjä menee osoitteeseen /reminders/, Django suorittaa reminders-toiminnon.
    # Tämä on yleensä sivu, jossa näkyvät lääkemuistutukset (lista ja mahdollinen lisäys).
    # name="reminders" antaa reitille nimen, jotta linkkejä voi tehdä helposti (ilman kovaa osoitetta).
    path("reminders/", reminders, name="reminders"),

    # Reitti: "reminders/<int:pk>/delete/"
    # Tässä osoitteessa on mukana muuttuva osa: <int:pk>
    # - int tarkoittaa: tähän tulee numero
    # - pk tarkoittaa: muistutuksen tunniste (ID), jolla löydetään oikea muistutus
    # Esimerkki: /reminders/5/delete/ -> poistaa muistutuksen, jonka ID on 5
    # Kun käyttäjä menee tähän osoitteeseen, Django suorittaa reminder_delete-toiminnon.
    # name="reminder_delete" antaa reitille nimen, jotta poistoon voi tehdä linkin/painikkeen helposti.
    path("reminders/<int:pk>/delete/", reminder_delete, name="reminder_delete"),
]
