from facade.sifreleme_facade import SifrelemeFacade

from factory.sifreleme_factory import SifrelemeFactory

from strategy.sifreleme_baglam import (
    SifrelemeBaglami
)

from observer.olay_yayici import OlayYayici
from observer.log_gozlemci import LogGozlemci
from observer.zaman_gozlemci import (
    ZamanGozlemci
)


algoritma = "AES"

metin = "Merhaba Dünya"


# Observer
yayici = OlayYayici()

yayici.gozlemci_ekle(
    LogGozlemci()
)

yayici.gozlemci_ekle(
    ZamanGozlemci()
)


# Strategy
sifreleyici = (
    SifrelemeFactory
    .sifreleyici_olustur(algoritma)
)

baglam = (
    SifrelemeBaglami(sifreleyici)
)


yayici.bildir(
    "Şifreleme işlemi başladı"
)

sifreli = (
    baglam
    .sifrele(metin)
)

yayici.bildir(
    "Şifreleme işlemi tamamlandı"
)

print("\nŞifreli Veri:")
print(sifreli)


cozulmus = (
    baglam
    .coz(sifreli)
)

print("\nÇözülmüş Veri:")
print(cozulmus)