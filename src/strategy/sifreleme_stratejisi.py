from abc import ABC, abstractmethod


class SifrelemeStratejisi(ABC):

    @abstractmethod
    def sifrele(self, veri: str) -> str:
        pass

    @abstractmethod
    def coz(self, sifreli_veri: str) -> str:
        pass