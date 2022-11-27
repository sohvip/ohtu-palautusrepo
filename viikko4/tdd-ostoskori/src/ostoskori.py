from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoskori = {}
        self._maara = 0
        self._hinta = 0
        self._kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self._maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self._hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if self._ostoskori.get(lisattava.nimi()) is None:
            self._ostoskori[lisattava.nimi()] = Ostos(lisattava)
            self._kori.append(self._ostoskori[lisattava.nimi()])
        else:
            self._ostoskori[lisattava.nimi()].muuta_lukumaaraa(1)
        self._maara += 1
        self._hinta += lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        self._hinta -= poistettava.hinta()
        self._maara -= 1
        self._ostoskori[poistettava.nimi()].muuta_lukumaaraa(-1)
        if self._ostoskori[poistettava.nimi()].lukumaara() == 0:
            self._kori.remove(self._ostoskori[poistettava.nimi()])
            del self._ostoskori[poistettava.nimi()]

    def tyhjenna(self):
        self._ostoskori.clear()
        self._maara = 0
        self._hinta = 0
        self._kori.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
