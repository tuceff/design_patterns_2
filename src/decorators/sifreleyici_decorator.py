from strategy.sifreleme_stratejisi import SifrelemeStratejisi


class SifreleyiciDekorator(SifrelemeStratejisi):
    """Şifreleme dekoratörlerinin temel sınıfı."""

    def __init__(
        self, sifreleyici: SifrelemeStratejisi
    ) -> None:
        self._sifreleyici = sifreleyici

    def sifrele(self, veri: str) -> str:
        return self._sifreleyici.sifrele(veri)

    def coz(self, veri: str) -> str:
        return self._sifreleyici.coz(veri)