# Tuodaan Djangosta valmiita aputoimintoja:
# - render = tekee HTML-sivun ja palauttaa sen käyttäjälle
# - redirect = ohjaa käyttäjän toiseen osoitteeseen (esim. takaisin listaan)
# - get_object_or_404 = hakee objektin tietokannasta tai palauttaa 404-virheen, jos sitä ei löydy
from django.shortcuts import render, redirect, get_object_or_404

# Tuodaan koristelija (decorator), jolla voidaan vaatia tietty HTTP-metodi:
# require_POST = sallii tämän näkymän (view) käytön vain POST-pyynnöllä (turvallisempi esim. poistossa)
from django.views.decorators.http import require_POST

# Tuodaan oma tietokantamalli (model) tästä sovelluksesta:
# MedicationReminder = lääkemuistutus, joka tallentuu tietokantaan
from .models import MedicationReminder

# Tuodaan oma lomake (form) tästä sovelluksesta:
# MedicationReminderForm = lomake, jolla käyttäjä syöttää uuden muistutuksen tiedot
from .forms import MedicationReminderForm


# Tämä funktio käsittelee "muistutukset" -sivun.
# Se näyttää lomakkeen ja listan olemassa olevista muistutuksista.
def reminders(request):
    """
    Näyttää lomakkeen + listan.
    POST: lisää uuden muistutuksen (PRG-malli).
    """
    # Docstring kertoo lyhyesti, mitä tämä toiminto tekee:
    # - Näyttää lomakkeen ja listan
    # - Jos käyttäjä lähettää lomakkeen (POST), lisätään uusi muistutus
    # - PRG-malli = Post -> Redirect -> Get (lähetä -> ohjaa -> näytä)
    #   Tämä estää saman muistutuksen lisääntymisen, jos sivu päivitetään.

    # Tarkistetaan, onko käyttäjä lähettänyt lomakkeen (POST-pyyntö).
    if request.method == "POST":

        # Tehdään lomake ja täytetään se käyttäjän lähettämillä tiedoilla.
        # request.POST sisältää lomakkeen kenttien arvot.
        form = MedicationReminderForm(request.POST)

        # Tarkistetaan, onko lomake oikein täytetty (validi).
        if form.is_valid():

            # Tallennetaan uusi muistutus tietokantaan.
            form.save()

            # Ohjataan käyttäjä takaisin muistutussivulle.
            # Tämä on PRG-mallin "Redirect"-vaihe.
            return redirect("reminders")

