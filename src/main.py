from facade.sifreleme_facade import SifrelemeFacade


sistem = SifrelemeFacade()

algoritma = "AES"  # "RSA" veya "BASE64"

metin = "Merhaba Dünya"

print("Aktif Algoritma:")
print(algoritma)

sifreli = sistem.sifrele(algoritma, metin)

print("\nŞifreli Veri:")
print(sifreli)

cozulmus = sistem.coz(algoritma, sifreli)

print("\nÇözülmüş Veri:")
print(cozulmus)