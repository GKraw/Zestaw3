# Napisac program realizujacy mnozenie macierzy (gdzie macierze sa reprezentowane przez listy)

def mnozenie(a, b):
    # Sprawdzenie zgodności wymiarów
    if len(a[0]) != len(b):
        print("Error: Liczba kolumn macierzy A musi być równa liczbie wierszy macierzy B.")
        return None

    # Inicjalizacja macierzy wynikowej (0 dla wszystkich elementów)
    wynik = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    # Mnożenie macierzy
    for i in range(len(a)):  # Wiersze macierzy A
        for j in range(len(b[0])):  # Kolumny macierzy B
            for k in range(len(b)):  # Wspólny wymiar (kolumny A / wiersze B)
                wynik[i][j] += a[i][k] * b[k][j]

    return wynik


# Przykładowe dane
a = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

b = [
    [3, 3, 3],
    [2, 2, 2],
    [1, 1, 1]
]

# Wynik
print(mnozenie(a, b))
