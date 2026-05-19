from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


class AESSifreleyici:

    def __init__(self):

        self.anahtar = b"1234567890123456"
    def sifrele(self, veri):

        iv = get_random_bytes(16)

        sifreleyici = AES.new(
            self.anahtar,
            AES.MODE_CBC,
            iv
        )

        sifreli_veri = sifreleyici.encrypt(
            pad(veri.encode(), AES.block_size)
        )

        sonuc = base64.b64encode(
            iv + sifreli_veri
        ).decode()

        return sonuc

    def coz(self, sifreli_veri):

        ham_veri = base64.b64decode(
            sifreli_veri
        )

        iv = ham_veri[:16]

        sifreli_kisim = ham_veri[16:]

        sifreleyici = AES.new(
            self.anahtar,
            AES.MODE_CBC,
            iv
        )

        cozulmus = unpad(
            sifreleyici.decrypt(sifreli_kisim),
            AES.block_size
        )

        return cozulmus.decode()