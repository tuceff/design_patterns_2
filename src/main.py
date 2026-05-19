from factory.sifreleme_factory import (
    SifrelemeFactory
)


algoritma = "AES"  # "RSA" veya "BASE64" olarak değiştirilebilir

sifreleyici = (
    SifrelemeFactory
    .sifreleyici_olustur(algoritma)
)

metin = "Merhaba Dünya"

print("Aktif Algoritma:")
print(algoritma)

sifreli = sifreleyici.sifrele(metin)

print("\nŞifreli Veri:")
print(sifreli)

cozulmus = sifreleyici.coz(sifreli)

print("\nÇözülmüş Veri:")
print(cozulmus)