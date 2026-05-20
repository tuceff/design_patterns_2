from factory.sifreleme_factory import SifrelemeFactory
from decorators.log_decorator import LogDekorator
from decorators.sure_decorator import SureDekorator
from strategy.sifreleme_stratejisi import SifrelemeStratejisi


class SifrelemeFacade:
    """Factory, Decorator ve Strategy örüntülerine basit erişim sağlar."""

    def _hazirla(
        self, algoritma: str
    ) -> SifrelemeStratejisi:
        sifreleyici = SifrelemeFactory.sifreleyici_olustur(algoritma)
        sifreleyici = LogDekorator(sifreleyici)
        sifreleyici = SureDekorator(sifreleyici)
        return sifreleyici

    def sifrele(
        self, algoritma: str, veri: str
    ) -> str:
        return self._hazirla(algoritma).sifrele(veri)

    def coz(
        self, algoritma: str, veri: str
    ) -> str:
        return self._hazirla(algoritma).coz(veri)