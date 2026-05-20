import time
from datetime import datetime
from observer.gozlemci import Gozlemci


class ZamanGozlemci(Gozlemci):

    def guncelle(self, mesaj: str) -> None:
        zaman = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        print(f"[ZAMAN {zaman}]: {mesaj}")