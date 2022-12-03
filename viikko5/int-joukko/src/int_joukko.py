KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = []
        self.lukujen_maara = 0

    def kuuluu(self, luku):
        vastaus = luku in self.lukujono
        return vastaus

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False
        if self.mahtavuus() >= self.kapasiteetti:
            self.kapasiteetti += self.kasvatuskoko
        self.lukujono.append(luku)
        return True

    def poista(self, luku):
        if self.kuuluu(luku):
            self.lukujono.remove(luku)
            return True
        return False

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return self.lukujono

    @staticmethod
    def yhdiste(lista_a, lista_b):
        joukko = IntJoukko()
        
        for i in lista_a.to_int_list():
            joukko.lisaa(i)
        for i in lista_b.to_int_list():
            if i not in joukko.to_int_list():
                joukko.lisaa(i)
        return joukko

    @staticmethod
    def leikkaus(lista_a, lista_b):
        joukko = IntJoukko()
        
        for i in lista_a.to_int_list():
            if i in lista_b.to_int_list():
                joukko.lisaa(i)
        return joukko

    @staticmethod
    def erotus(lista_a, lista_b):
        joukko = IntJoukko()

        for i in lista_a.to_int_list():
            if i not in lista_b.to_int_list():
                joukko.lisaa(i)
        return joukko

    def __str__(self):
        if self.mahtavuus() == 0:
            return "{}"
        elif self.mahtavuus() == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in self.lukujono[0:-1]:
                tuotos = tuotos + str(i)
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[-1])
            tuotos = tuotos + "}"
            return tuotos
