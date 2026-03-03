Tämä projekti on yksinkertainen lääkemuistutin‑sovellus, joka on rakennettu Djangolla. 
Sovelluksella voi lisätä lääkemuistutuksia, katsoa ne listana ja poistaa vanhoja muistutuksia. Kaikki tiedot tallentuvat automaattisesti tietokantaan.

Sovelluksessa voi täyttää lomakkeen, jossa kysytään lääkkeen nimi, annostus, kellonaika ja vapaavalintainen lisäohje. Kun käyttäjä painaa tallenna-nappia, muistutus siirtyy tietokantaan ja näkyy heti listassa. 
Jokaisen muistutuksen kohdalla näkyy selkeä Poista-painike.

Sovelluksessa on yksinkertainen käyttöliittymä. Teksti on isoa (20px), kontrastia on mietitty ja käyttö onnistuu myös pelkällä näppäimistöllä. Sivulla on myös “siirry sisältöön” -linkki ja selkeät virheilmoitukset, jotka auttavat käyttöä esimerkiksi ruudunlukijan kanssa. Tämä lisää sovelluksen saavutettavuutta.

Tietokanta toimii automaattisesti Djangon avulla. Sovellettu malli tallentaa lääkkeen nimen, annostuksen, kellonajan, ohjeet ja luontiajan. 

Koodi on jaettu seuraavasti: models-tiedosto sisältää tietokantamallin, views-tiedosto sisältää sivujen logiikan, forms hoitaa lomakkeet, templates sisältävät HTML-sivut ja static-kansio sisältää CSS-tyylit. 

Sovelluksen voi käynnistää aktivoimalla virtuaaliympäristön, asentamalla tarvittavat paketit, tekemällä tietokantamigraatiot ja käynnistämällä Djangon kehityspalvelimen. 

Django projektin rakenne: 

<img width="633" height="631" alt="image" src="https://github.com/user-attachments/assets/ba86559b-303f-4c2b-accb-2b6e0a7ebec1" />





