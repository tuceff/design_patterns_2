class SifreleyiciDekorator:

    def __init__(self, sifreleyici):
        self.sifreleyici = sifreleyici

    def sifrele(self, veri):
        return self.sifreleyici.sifrele(veri)

    def coz(self, veri):
        return self.sifreleyici.coz(veri)