from threading import Lock
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey


class RSAAnahtarYoneticisi:
    """RSA anahtar çiftini tek örnek olarak yönetir."""

    _ornek: "RSAAnahtarYoneticisi | None" = None
    _kilit: Lock = Lock()

    def __new__(cls) -> "RSAAnahtarYoneticisi":
        if cls._ornek is None:
            with cls._kilit:
                # Double-checked locking
                if cls._ornek is None:
                    inst = super().__new__(cls)
                    inst._ozel_anahtar = RSA.generate(2048)
                    inst._genel_anahtar = (
                        inst._ozel_anahtar.publickey()
                    )
                    cls._ornek = inst
        return cls._ornek

    @property
    def ozel_anahtar(self) -> RsaKey:
        return self._ozel_anahtar

    @property
    def genel_anahtar(self) -> RsaKey:
        return self._genel_anahtar