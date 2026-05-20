from facade.sifreleme_facade import SifrelemeFacade
from factory.sifreleme_factory import SifrelemeFactory
from strategy.sifreleme_baglam import SifrelemeBaglami
from observer.olay_yayici import OlayYayici
from observer.log_gozlemci import LogGozlemci
from observer.zaman_gozlemci import ZamanGozlemci


def main() -> None:
    algoritma: str = "AES"
    metin: str = "Merhaba Dünya"

    # Observer kurulumu
    yayici = OlayYayici()
    yayici.gozlemci_ekle(LogGozlemci())
    yayici.gozlemci_ekle(ZamanGozlemci())

    # Strategy + Factory kurulumu
    sifreleyici = SifrelemeFactory.sifreleyici_olustur(algoritma)
    baglam = SifrelemeBaglami(sifreleyici)

    yayici.bildir("Şifreleme işlemi başladı")
    sifreli: str = baglam.sifrele(metin)
    yayici.bildir("Şifreleme işlemi tamamlandı")

    print(f"\nŞifreli Veri:\n{sifreli}")

    yayici.bildir("Çözme işlemi başladı")
    cozulmus: str = baglam.coz(sifreli)
    yayici.bildir("Çözme işlemi tamamlandı")

    print(f"\nÇözülmüş Veri:\n{cozulmus}")


if __name__ == "__main__":
    main()