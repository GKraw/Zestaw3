# Stworzyć dataclass w zadaniu 2

# Zad 2
# Napisac prosta klase przechowujaca np. dane osobowe (imie, nazwisko, adres zamieszkania, kod pocztowy, pesel)
# i metode zapisujaca obiekty typu tej klasy do json, oraz metode odczytuja json'a i ladujace dane do klasy


from dataclasses import dataclass
import json

@dataclass
class DaneOsobowe:
    imie: str
    nazwisko: str
    adres: str
    kod_pocztowy: str
    pesel: str

    # Metoda zapisująca dane do pliku JSON
    def zapisz_do_json(self, nazwa_pliku: str):
        with open(nazwa_pliku, 'w') as plik:
            json.dump(self.__dict__, plik)  # self.__dict__ zamienia obiekt na słownik

    # Metoda odczytująca dane z pliku JSON i zwracająca nową instancję klasy
    @classmethod
    def odczytaj_z_json(cls, nazwa_pliku: str):
        with open(nazwa_pliku, 'r') as plik:
            dane = json.load(plik)  # Wczytujemy dane jako słownik
        return cls(**dane)  # Tworzymy nową instancję klasy na podstawie słownika


# Przykład użycia
# Tworzymy obiekt z danymi osobowymi
osoba = DaneOsobowe(
    imie="Jan",
    nazwisko="Kowalski",
    adres="ul. Warszawska 1, Kraków",
    kod_pocztowy="30-001",
    pesel="12345678901"
)

# Zapisujemy dane do pliku JSON
osoba.zapisz_do_json("osoba.json")

# Odczytujemy dane z pliku JSON i tworzymy nowy obiekt
nowa_osoba = DaneOsobowe.odczytaj_z_json("osoba.json")

# Wyświetlamy wczytane dane
print(nowa_osoba)
