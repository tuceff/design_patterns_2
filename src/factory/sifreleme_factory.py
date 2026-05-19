from sifreleyiciler.aes_sifreleyici import (
    AESSifreleyici
)

from sifreleyiciler.rsa_sifreleyici import (
    RSASifreleyici
)

from sifreleyiciler.base64_sifreleyici import (
    Base64Sifreleyici
)


class SifrelemeFactory:

    @staticmethod
    def sifreleyici_olustur(algoritma):

        if algoritma == "AES":
            return AESSifreleyici()

        elif algoritma == "RSA":
            return RSASifreleyici()

        elif algoritma == "BASE64":
            return Base64Sifreleyici()

        else:
            raise Exception(
                "Desteklenmeyen algoritma"
            )