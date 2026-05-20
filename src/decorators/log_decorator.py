from decorators.sifreleyici_decorator import SifreleyiciDekorator


class LogDekorator(SifreleyiciDekorator):

    def sifrele(self, veri):

        print("Şifreleme başladı")

        sonuc = self.sifreleyici.sifrele(veri)

        print("Şifreleme bitti")

        return sonuc

    def coz(self, veri):

        print("Çözme başladı")

        sonuc = self.sifreleyici.coz(veri)

        print("Çözme bitti")

        return sonuc