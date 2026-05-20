from abc import ABC, abstractmethod


class Gozlemci(ABC):

    @abstractmethod
    def guncelle(self, mesaj: str):
        pass