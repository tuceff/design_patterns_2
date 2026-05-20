from observer.gozlemci import Gozlemci


class LogGozlemci(Gozlemci):

    def guncelle(self, mesaj: str) -> None:
        print(f"[LOG]: {mesaj}")