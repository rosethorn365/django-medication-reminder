Tämä projekti on yksinkertainen lääkemuistutin‑sovellus, joka on rakennettu Djangolla. 
Sovelluksella voi lisätä lääkemuistutuksia, katsoa ne listana ja poistaa vanhoja muistutuksia. Kaikki tiedot tallentuvat automaattisesti tietokantaan.

Sovelluksessa voi täyttää lomakkeen, jossa kysytään lääkkeen nimi, annostus, kellonaika ja vapaavalintainen lisäohje. Kun käyttäjä painaa tallenna-nappia, muistutus siirtyy tietokantaan ja näkyy heti listassa. 
Jokaisen muistutuksen kohdalla näkyy selkeä Poista-painike.

Sovelluksessa on yksinkertainen käyttöliittymä. Teksti on isoa (20px), kontrastia on mietitty ja käyttö onnistuu myös pelkällä näppäimistöllä. Sivulla on myös “siirry sisältöön” -linkki ja selkeät virheilmoitukset, jotka auttavat käyttöä esimerkiksi ruudunlukijan kanssa. Tämä lisää sovelluksen saavutettavuutta.

Tietokanta toimii automaattisesti Djangon avulla. Sovellettu malli tallentaa lääkkeen nimen, annostuksen, kellonajan, ohjeet ja luontiajan. 

Koodi on jaettu seuraavasti: models-tiedosto sisältää tietokantamallin, views-tiedosto sisältää sivujen logiikan, forms hoitaa lomakkeet, templates sisältävät HTML-sivut ja static-kansio sisältää CSS-tyylit. 

Sovelluksen voi käynnistää aktivoimalla virtuaaliympäristön, asentamalla tarvittavat paketit, tekemällä tietokantamigraatiot ja käynnistämällä Djangon kehityspalvelimen. 

Django projektin rakenne: 

DJANGO_DEMO/
├─ demo/                 # Django-app (varsinainen lääkemuistutin)
│  ├─ migrations/        # tietokantamigraatiot (001_initial.py)
│  ├─ static/demo/       # CSS ja muut staattiset tiedostot
│  │  └─ style.css
│  ├─ templates/demo/    # HTML-templatet
│  │  ├─ hello.html
│  │  └─ reminders.html
│  ├─ admin.py           # admin-näkymän rekisteröinti
│  ├─ apps.py            # app-konfiguraatio
│  ├─ forms.py           # lomakkeet + validointi
│  ├─ models.py          # tietokantamallit
│  ├─ urls.py            # appin URL-reitit (esim. /reminders/)
│  ├─ views.py           # näkymät (CRUD-logiikka)
│  └─ ...
├─ myproject/            # Django-projekti (asetukset ja pääreititys)
│  ├─ settings.py        # DB-asetukset, middleware, static, templates...
│  ├─ urls.py            # project-level URLConf (include demo.urls)
│  ├─ wsgi.py / asgi.py  # deploy/serving entrypointit
├─ db.sqlite3            # käytössä oleva tietokanta (kehityksessä)
├─ manage.py             # Django CLI (runserver, migrate, ...)
├─ requirements.txt      # riippuvuudet
└─ venv/                 # virtuaaliympäristö




