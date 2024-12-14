# Napisać obiektowo prosty dekorator na funkcji wypisującej jakiś string,
# a celem dekoratora jest zamiana liter w napisie na duże litery

# Definiujemy dekorator
def zamien_na_duze(funkcja):
    def dekorowana_funkcja():
        wynik = funkcja()  # Wywołujemy oryginalną funkcję
        return wynik.upper()  # Zamieniamy wynik na wielkie litery
    return dekorowana_funkcja

# Funkcja, którą udekorujemy
@zamien_na_duze
def wypisz_napis():
    return "to jest przykładowy napis"

# Wywołanie udekorowanej funkcji
print(wypisz_napis())
