class OlayYayici:

    def __init__(self):
        self.gozlemciler = []

    def gozlemci_ekle(self, gozlemci):
        self.gozlemciler.append(gozlemci)

    def bildir(self, mesaj: str):

        for gozlemci in self.gozlemciler:
            gozlemci.guncelle(mesaj)