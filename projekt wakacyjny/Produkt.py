class Produkt():
    def __init__(self,kod,nazwa,waga):
        self.kod = kod
        self.nazwa = nazwa
        self.waga = waga

    def podaj_kod(self):
        return self.kod

    def podaj_nazwe(self):
        return self.nazwa

    def podaj_wage(self):
        return self.waga