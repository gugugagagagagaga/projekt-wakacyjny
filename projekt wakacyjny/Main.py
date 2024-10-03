from Uzytkownik import Uzytkownik
import json

class Main():
    def start(self):
        print("Proces logowania:")
        try:
            nazwa = input('Podaj nazwę użytkownika: ')
            if not nazwa:
                raise ValueError('Nazwa użytkownika nie może być pusta')
            
            haslo = input('Podaj hasło użytkownika: ')
            if not haslo:
                raise ValueError('Hasło nie powinno być puste')
        except ValueError as e:
            print(e)
        try:
            with open('uzytkownicy.json') as plikOdczyt:
                print("odczytuje plik")
                zawartosc = json.load(plikOdczyt)
                for uzytkownik in zawartosc["uzytkownicy"]:
                    if uzytkownik["nazwa"] == nazwa and uzytkownik["haslo"] == haslo:
                        print("zalogowano pomyślnie")
                        if uzytkownik["rola"] == "admin":
                            print("Możesz robić co chcesz")

                            print("Wskaż nazwę użytkownika, którego dane chcesz zmienić:")

                            for u in zawartosc["uzytkownicy"]:
                                print(u["nazwa"], end=", ")
                            print("")
                            user = input("nazwa uzytkownik: ")

                            print("Co chcesz zrobić?:")
                            print("1. zmiana nazwy użytkownika")
                            print("2. zmiana hasła użytkownika")
                            print("3. zmiana wieku użytkownika")
                            print("4. zmiana uprawnień użytkownika")
                            decyzja = input("decyzja: ")

                            if decyzja==1:
                                zawartosc["uzytkownicy"]["..."]["nazwa"] = input("nowa nazwa: ")
                            if decyzja==2:
                                zawartosc["uzytkownicy"]["..."]["haslo"] = input("nowe haslo: ")
                            if decyzja==3:
                                zawartosc["uzytkownicy"]["..."]["wiek"] = int(input("aktualizacja wieku: "))
                            if decyzja==4:
                                zawartosc["uzytkownicy"]["..."]["rola"] = int(input("nazwa roli z uprawnieniami: "))
                            
                        
                            with open('uzytkownicy.json', 'w') as plikZapis:
                                json.dump(zawartosc, plikZapis)
                       
        except IOError as e:
            print("Nie znaleziono pliku")

        '''
        uzytkownik1 = Uzytkownik("Mikolaj", "123")
        #print(uzytkownik1.podaj_nazwe())
        #print(uzytkownik1.podaj_haslo())
        
        if nazwa == uzytkownik1.podaj_nazwe():
            print("jest taki użytkownik")
        else:
            print("nie ma takiego użytkownika")
        #print("Działa!")
        '''

if __name__ == "__main__":
    main = Main()
    main.start()
