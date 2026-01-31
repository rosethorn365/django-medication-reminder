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

Djangon hyödyt:
Django on erinomainen valinta tietokantasovelluksiin, koska se tarjoaa selkeän ORM‑kerroksen, joka mahdollistaa tietojen käsittelyn ilman SQL‑koodia, hoitaa migraatiot automaattisesti ja tukee useita tietokantoja saumattomasti. Frameworkin mukana tuleva admin‑paneeli nopeuttaa CRUD‑toimintojen kehitystä, ja sisäänrakennettu tietoturva — kuten SQL‑injektion, CSRF‑ ja XSS‑hyökkäysten esto — tekee sovelluksista turvallisia oletuksena. Djangon selkeä models–views–templates‑rakenne, saavutettavuusystävälliset templatet sekä pitkä kehityshistoria ja laaja tuotantokäyttö tekevät siitä luotettavan ja helposti ylläpidettävän ratkaisun kaiken kokoisiin tietokantapohjaisiin projekteihin.

Djangon haasteet: 

Vaikka Django on turvallinen ja “secure‑by‑default”, viime vuosien CVE‑haavoittuvuudet osoittavat, että myös sen ORM ja ydinrakenteet voivat altistua riskeille. Vuonna 2025 löydettiin useita vakavia SQL‑injektiohaavoittuvuuksia, erityisesti tilanteissa joissa käyttäjän syöte päätyy dictionary‑laajennuksena QuerySet‑kutsuihin. Näitä ovat mm. CVE‑2025‑64459, joka mahdollistaa ehtorakenteiden manipuloinnin ja SQL‑kyselyiden injektoinnin, sekä CVE‑2025‑59681, joka koskee annotate/alias‑kutsujen injektiota MySQL/MariaDB‑ympäristöissä. Lisäksi joissain PostgreSQL‑tilanteissa FilteredRelation‑toiminnallisuus on altistunut SQL‑injektiolle (CVE‑2025‑13372). [cyberpress.org] [djangoproject.com] [djangoproject.com]
Django on kokenut myös DoS‑haavoittuvuuksia, kuten Windows‑järjestelmiin vaikuttavan Unicode‑normalisointivirheen (CVE‑2025‑64458)  sekä XML‑serializerin algoritmisen kompleksisuuden aiheuttaman kuormittumisen (CVE‑2025‑64460). Lisäksi tietyt kehitystyökalut, kuten archive.extract(), ovat olleet alttiita directory traversal ‑hyökkäyksille (CVE‑2025‑59682). [cyberpress.org] [djangoproject.com] [djangoproject.com]
Frameworkin ulkopuolella monet tietoturvariskit johtuvat kehittäjän tekemistä konfiguraatio‑ tai validaatiovirheistä. Yleisiä riskejä ovat XSS, CSRF, clickjacking ja heikko sessiohallinta, mikä korostaa oikeiden suojausten (esim. CSP, csrf_token, X_FRAME_OPTIONS) tärkeyttä. [linkedin.com]
