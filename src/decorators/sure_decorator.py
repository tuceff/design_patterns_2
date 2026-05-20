import time
from decorators.sifreleyici_decorator import SifreleyiciDekorator


class SureDekorator(SifreleyiciDekorator):

    def sifrele(self, veri):

        basla = time.time()

        sonuc = self.sifreleyici.sifrele(veri)

        bitis = time.time()

        print(f"Süre: {bitis - basla:.6f} saniye")

        return sonuc

    def coz(self, veri):

        basla = time.time()

        sonuc = self.sifreleyici.coz(veri)

        bitis = time.time()

        print(f"Süre: {bitis - basla:.6f} saniye")

        return sonuc