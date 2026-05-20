import time

from observer.gozlemci import Gozlemci


class ZamanGozlemci(Gozlemci):

    def guncelle(self, mesaj: str):
        print(f"[ZAMAN]: {mesaj}")
        print(f"Bildirim Zamanı: {time.time()}")