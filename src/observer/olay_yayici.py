from observer.gozlemci import Gozlemci


class OlayYayici:

    def __init__(self) -> None:
        self._gozlemciler: list[Gozlemci] = []

    def gozlemci_ekle(
        self, gozlemci: Gozlemci
    ) -> None:
        if gozlemci not in self._gozlemciler:
            self._gozlemciler.append(gozlemci)

    def gozlemci_cikar(
        self, gozlemci: Gozlemci
    ) -> None:
        self._gozlemciler.remove(gozlemci)

    def bildir(self, mesaj: str) -> None:
        for gozlemci in list(self._gozlemciler):
            gozlemci.guncelle(mesaj)