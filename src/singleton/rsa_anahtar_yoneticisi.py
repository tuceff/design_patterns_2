from Crypto.PublicKey import RSA


class RSAAnahtarYoneticisi:

    _ornek = None

    def __new__(cls):

        if cls._ornek is None:

            cls._ornek = super().__new__(cls)

            # Anahtarlar sadece 1 kez oluşturulur
            cls._ornek.ozel_anahtar = RSA.generate(2048)

            cls._ornek.genel_anahtar = (
                cls._ornek.ozel_anahtar.publickey()
            )
            
        return cls._ornek