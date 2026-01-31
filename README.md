Tämä projekti on yksinkertainen ja helppokäyttöinen lääkemuistutin‑sovellus, joka on rakennettu Django-ohjelmistolla. 
Sovelluksella voi lisätä lääkemuistutuksia, katsoa ne listana ja poistaa vanhoja muistutuksia. Kaikki tiedot tallentuvat automaattisesti tietokantaan.

Sovelluksessa voi täyttää lomakkeen, jossa kysytään lääkkeen nimi, annostus, kellonaika ja mahdollinen lisäohje. Kun käyttäjä painaa Tallenna, muistutus siirtyy talteen ja näkyy heti listassa. 
Jokaisen muistutuksen kohdalla näkyy selkeä Poista-painike, jolla merkinnän saa helposti pois.

Sovelluksessa on selkeä ja saavutettava käyttöliittymä. Teksti on isoa (20px), kontrastia on mietitty ja käyttö onnistuu myös pelkällä näppäimistöllä. Sivulla on myös “siirry sisältöön” -linkki ja selkeät virheilmoitukset, jotka auttavat käyttöä esimerkiksi ruudunlukijan kanssa. Tämä tekee sovelluksesta helppokäyttöisen ihmisille, joilla on näkö- tai motorisia haasteita.
Sovelluksessa voi myös tulostaa kaikki muistutukset siistinä listana. Tulostusnäkymä piilottaa lomakkeen ja napit, ja näyttää vain selkeän lääkelistan. Tätä voi käyttää esimerkiksi lääkekorttina kotona tai hoitotyössä.

Tietokanta toimii automaattisesti Djangon avulla. Sovellettu malli tallentaa lääkkeen nimen, annostuksen, kellonajan, ohjeet ja luontiajan. Tietokannan hallinta ei vaadi käyttäjältä erikoisosaamista.

Koodi on jaettu selkeisiin osiin: models-tiedosto sisältää tietokantamallin, views-tiedosto sisältää sivujen logiikan, forms hoitaa lomakkeet, templates sisältävät HTML-sivut ja static-kansio sisältää CSS-tyylit. 
Projekti toimii kansiorakenteella.

Tämä projekti siis sisältää tietokannan, lomakkeet, CRUD-toiminnot, saavutettavan käyttöliittymän ja tulostusnäkymän. 
Sovellus tarjoaa perustason ratkaisun lääkkeiden muistamiseen.

Sovelluksen voi käynnistää aktivoimalla virtuaaliympäristön, asentamalla tarvittavat paketit, tekemällä tietokantamigraatiot ja käynnistämällä Djangon kehityspalvelimen. Selaimessa sovellus avautuu osoitteessa http://127.0.0.1:8000/reminders/
ja admin login http://127.0.0.1:8000/admin/demo/medicationreminder/
