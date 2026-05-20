from sifreleyiciler.aes_sifreleyici import AESSifreleyici
from sifreleyiciler.rsa_sifreleyici import RSASifreleyici
from sifreleyiciler.base64_sifreleyici import Base64Sifreleyici
from strategy.sifreleme_stratejisi import SifrelemeStratejisi


class SifrelemeFactory:

    _SIFRELEYICILER: dict[str, type[SifrelemeStratejisi]] = {
        "AES": AESSifreleyici,
        "RSA": RSASifreleyici,
        "BASE64": Base64Sifreleyici,
    }

    @staticmethod
    def sifreleyici_olustur(
        algoritma: str,
    ) -> SifrelemeStratejisi:

        sifreleyici_cls = SifrelemeFactory._SIFRELEYICILER.get(
            algoritma.upper()
        )

        if sifreleyici_cls is None:
            desteklenenler = ", ".join(
                SifrelemeFactory._SIFRELEYICILER.keys()
            )
            raise ValueError(
                f"Desteklenmeyen algoritma: '{algoritma}'. "
                f"Desteklenenler: {desteklenenler}"
            )

        return sifreleyici_cls()