# Napisac obiektowo program, ktory realizuje automat stanow (np. Mealy'ego albo Moore'a),
# czyli nalezy stworzyc odpowiednie klasy z funkcjami, a nastepnie z nich utworzyc konkretna przykladowe instancje

class MealyAutomat:
    def __init__(self):
        # Definicja początkowego stanu
        self.stan = "S0"

    # Funkcja przejścia stanów
    def przejscie(self, wejscie):
        if self.stan == "S0":
            if wejscie == 0:
                self.stan = "S0"
                return "A"
            elif wejscie == 1:
                self.stan = "S1"
                return "B"

        elif self.stan == "S1":
            if wejscie == 0:
                self.stan = "S2"
                return "C"
            elif wejscie == 1:
                self.stan = "S0"
                return "D"

        elif self.stan == "S2":
            if wejscie == 0:
                self.stan = "S1"
                return "E"
            elif wejscie == 1:
                self.stan = "S2"
                return "F"

    # Funkcja pomocnicza do wyświetlenia obecnego stanu
    def pokaz_stan(self):
        print(f"Aktualny stan: {self.stan}")


# Tworzymy instancję automatu
automat = MealyAutomat()

# Przykład wejść
wejscia = [0, 1, 0, 1, 1, 0]

# Przetwarzamy wejścia w pętli
print("Start automatu:")
for wejscie in wejscia:
    wynik = automat.przejscie(wejscie)
    automat.pokaz_stan()
    print(f"Wejście: {wejscie}, Wyjście: {wynik}")
