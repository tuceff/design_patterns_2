from decorators.sifreleyici_decorator import SifreleyiciDekorator


class LogDekorator(SifreleyiciDekorator):

    def sifrele(self, veri: str) -> str:
        print("[LOG] Şifreleme başladı")
        sonuc = super().sifrele(veri)
        print("[LOG] Şifreleme bitti")
        return sonuc

    def coz(self, veri: str) -> str:
        print("[LOG] Çözme başladı")
        sonuc = super().coz(veri)
        print("[LOG] Çözme bitti")
        return sonuc