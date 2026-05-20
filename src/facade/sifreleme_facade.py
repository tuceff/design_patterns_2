from factory.sifreleme_factory import SifrelemeFactory
from decorators.log_decorator import LogDekorator
from decorators.sure_decorator import SureDekorator


class SifrelemeFacade:

    def __init__(self):
        self.factory = SifrelemeFactory()

    def sifrele(self, algoritma, veri):

        sifreleyici = self.factory.sifreleyici_olustur(algoritma)

        sifreleyici = LogDekorator(sifreleyici)
        sifreleyici = SureDekorator(sifreleyici)

        return sifreleyici.sifrele(veri)

    def coz(self, algoritma, veri):

        sifreleyici = self.factory.sifreleyici_olustur(algoritma)

        sifreleyici = LogDekorator(sifreleyici)
        sifreleyici = SureDekorator(sifreleyici)

        return sifreleyici.coz(veri)