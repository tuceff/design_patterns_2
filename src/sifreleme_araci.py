from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# KÖTÜ TASARIM:
class SifrelemeAraci:

    def __init__(self):
        self.algoritma = "AES"

        # AES için sabit anahtar
        self.aes_key = b"1234567890123456"

        # RSA anahtarları
        self.rsa_private_key = RSA.generate(2048)
        self.rsa_public_key = self.rsa_private_key.publickey()

    # --------------------------------------------------
    # ŞİFRELEME
    # --------------------------------------------------
    def sifrele(self, veri):

        if self.algoritma == "AES":
            return self._aes_sifrele(veri)

        elif self.algoritma == "RSA":
            return self._rsa_sifrele(veri)

        elif self.algoritma == "BASE64":
            return self._base64_sifrele(veri)

        else:
            raise Exception("Desteklenmeyen algoritma")

    # --------------------------------------------------
    # ÇÖZME
    # --------------------------------------------------
    def coz(self, sifreli_veri):

        if self.algoritma == "AES":
            return self._aes_coz(sifreli_veri)

        elif self.algoritma == "RSA":
            return self._rsa_coz(sifreli_veri)

        elif self.algoritma == "BASE64":
            return self._base64_coz(sifreli_veri)

        else:
            raise Exception("Desteklenmeyen algoritma")

    # ==================================================
    # AES
    # ==================================================
    def _aes_sifrele(self, veri):

        iv = get_random_bytes(16)

        cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)

        sifreli = cipher.encrypt(
            pad(veri.encode(), AES.block_size)
        )

        sonuc = base64.b64encode(iv + sifreli).decode()

        return sonuc

    def _aes_coz(self, sifreli_veri):

        raw = base64.b64decode(sifreli_veri)

        iv = raw[:16]
        sifreli = raw[16:]

        cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)

        cozulmus = unpad(
            cipher.decrypt(sifreli),
            AES.block_size
        )

        return cozulmus.decode()

    # ==================================================
    # RSA
    # ==================================================
    def _rsa_sifrele(self, veri):

        cipher = PKCS1_OAEP.new(self.rsa_public_key)

        sifreli = cipher.encrypt(veri.encode())

        return base64.b64encode(sifreli).decode()

    def _rsa_coz(self, sifreli_veri):

        cipher = PKCS1_OAEP.new(self.rsa_private_key)

        sifreli_bytes = base64.b64decode(sifreli_veri)

        cozulmus = cipher.decrypt(sifreli_bytes)

        return cozulmus.decode()

    # ==================================================
    # BASE64
    # ==================================================
    def _base64_sifrele(self, veri):

        return base64.b64encode(
            veri.encode()
        ).decode()

    def _base64_coz(self, sifreli_veri):

        return base64.b64decode(
            sifreli_veri.encode()
        ).decode()


# ======================================================
# TEST
# ======================================================

sifrele = SifrelemeAraci()

metin = "Merhaba Dünya"

print("Aktif Algoritma:", sifrele.algoritma)

sifreli = sifrele.sifrele(metin)

print("\nŞifreli Veri:")
print(sifreli)

cozulmus = sifrele.coz(sifreli)

print("\nÇözülmüş Veri:")
print(cozulmus)