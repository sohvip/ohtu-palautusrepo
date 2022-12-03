class Erotus:
    def __init__(self, sovellus, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote

    def suorita(self):
        self.syote = int(self.lue_syote())
        self.sovellus.miinus(self.syote)
