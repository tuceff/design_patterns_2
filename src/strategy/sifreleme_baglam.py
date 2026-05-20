from strategy.sifreleme_stratejisi import SifrelemeStratejisi


class SifrelemeBaglami:
    """Şifreleme stratejisini kullanan bağlam sınıfı."""

    def __init__(
        self, strateji: SifrelemeStratejisi
    ) -> None:
        self._strateji = strateji

    @property
    def strateji(self) -> SifrelemeStratejisi:
        return self._strateji

    def strateji_degistir(
        self, yeni_strateji: SifrelemeStratejisi
    ) -> None:
        self._strateji = yeni_strateji

    def sifrele(self, veri: str) -> str:
        return self._strateji.sifrele(veri)

    def coz(self, sifreli_veri: str) -> str:
        return self._strateji.coz(sifreli_veri)