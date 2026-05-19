import base64


class Base64Sifreleyici:

    def sifrele(self, veri):

        return base64.b64encode(
            veri.encode()
        ).decode()
    def coz(self, sifreli_veri):

        return base64.b64decode(
            sifreli_veri.encode()
        ).decode()