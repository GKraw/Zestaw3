# Napisac prosta klase przechowujaca np. dane osobowe (imie, nazwisko, adres zamieszkania, kod pocztowy, pesel)
# i metode zapisujaca obiekty typu tej klasy do json, oraz metode odczytuja json'a i ladujace dane do klasy


import json

class DaneOsobowe:
    def __init__(self, imie, nazwisko, adres, kod_pocztowy, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.kod_pocztowy = kod_pocztowy
        self.pesel = pesel

    # Metoda do zapisania obiektu do JSON
    def zapisz_do_json(self, plik):
        dane = {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "adres": self.adres,
            "kod_pocztowy": self.kod_pocztowy,
            "pesel": self.pesel
        }
        with open(plik, 'w') as f:
            json.dump(dane, f, indent=4)  # Zapis formatowaniem
        print(f"Dane zapisano do pliku {plik}")

    # Metoda do odczytu JSON i załadowania danych do obiektu
    @staticmethod
    def odczytaj_z_json(plik):
        with open(plik, 'r') as f:
            dane = json.load(f)
        # Tworzymy nowy obiekt klasy na podstawie odczytanych danych
        return DaneOsobowe(
            dane["imie"],
            dane["nazwisko"],
            dane["adres"],
            dane["kod_pocztowy"],
            dane["pesel"]
        )

    # Opcjonalna metoda do wypisania danych
    def __str__(self):
        return f"{self.imie} {self.nazwisko}, Adres: {self.adres}, Kod: {self.kod_pocztowy}, PESEL: {self.pesel}"


# Przykład użycia
# Tworzymy obiekt
osoba = DaneOsobowe("Jan", "Kowalski", "ul. Warszawska 10, Kraków", "30-001", "12345678901")

# Zapisujemy do pliku JSON
osoba.zapisz_do_json("dane_osobowe.json")

# Wczytujemy dane z pliku JSON
nowa_osoba = DaneOsobowe.odczytaj_z_json("dane_osobowe.json")
print("Wczytane dane:")
print(nowa_osoba)
