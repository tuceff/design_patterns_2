from observer.gozlemci import Gozlemci


class LogGozlemci(Gozlemci):

    def guncelle(self, mesaj: str):
        print(f"[LOG]: {mesaj}")