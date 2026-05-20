import time
from decorators.sifreleyici_decorator import SifreleyiciDekorator


class SureDekorator(SifreleyiciDekorator):

    def sifrele(self, veri: str) -> str:
        basla = time.perf_counter()
        sonuc = super().sifrele(veri)
        sure = time.perf_counter() - basla
        print(f"[SÜRE] Şifreleme: {sure:.6f}s")
        return sonuc

    def coz(self, veri: str) -> str:
        basla = time.perf_counter()
        sonuc = super().coz(veri)
        sure = time.perf_counter() - basla
        print(f"[SÜRE] Çözme: {sure:.6f}s")
        return sonuc