class SifrelemeBaglami:

    def __init__(self, strateji):
        self.strateji = strateji

    def strateji_degistir(self, yeni_strateji):
        self.strateji = yeni_strateji

    def sifrele(self, veri: str) -> str:
        return self.strateji.sifrele(veri)

    def coz(self, sifreli_veri: str) -> str:
        return self.strateji.coz(sifreli_veri)