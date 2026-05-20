from abc import ABC, abstractmethod


class SifrelemeStratejisi(ABC):
    """Şifreleme algoritmaları için temel arayüz."""

    @abstractmethod
    def sifrele(self, veri: str) -> str:
        """Veriyi şifreler ve şifreli metni döner."""

    @abstractmethod
    def coz(self, sifreli_veri: str) -> str:
        """Şifreli veriyi çözer ve düz metni döner."""