from Crypto.Cipher import PKCS1_OAEP
import base64

from singleton.rsa_anahtar_yoneticisi import (
    RSAAnahtarYoneticisi
)


class RSASifreleyici:

    def __init__(self):

        self.anahtar_yoneticisi = (
            RSAAnahtarYoneticisi()
        )
        
    def sifrele(self, veri):

        sifreleyici = PKCS1_OAEP.new(
            self.anahtar_yoneticisi.genel_anahtar
        )

        sifreli_veri = sifreleyici.encrypt(
            veri.encode()
        )

        return base64.b64encode(
            sifreli_veri
        ).decode()

    def coz(self, sifreli_veri):

        sifreleyici = PKCS1_OAEP.new(
            self.anahtar_yoneticisi.ozel_anahtar
        )

        sifreli_bytes = base64.b64decode(
            sifreli_veri
        )

        cozulmus = sifreleyici.decrypt(
            sifreli_bytes
        )

        return cozulmus.decode()