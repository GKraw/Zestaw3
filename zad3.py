# Napisac algorytm Dijkstry (przechodzenie najkrotszej sciezki w grafie)

import heapq  # Przydatna do implementacji priorytetowej kolejki

def dijkstra(graph, start):
    # Słownik do przechowywania najkrótszych odległości
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Kolejka priorytetowa (w postaci krotki: (odległość, wierzchołek))
    priority_queue = [(0, start)]

    while priority_queue:
        # Pobieramy wierzchołek o najmniejszej odległości
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Jeśli odległość w kolejce jest większa niż znana, pomijamy ją
        if current_distance > distances[current_vertex]:
            continue

        # Sprawdzamy sąsiadów bieżącego wierzchołka
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Jeśli znaleźliśmy krótszą ścieżkę do sąsiada, aktualizujemy ją
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Przykładowy graf jako słownik
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Uruchamiamy algorytm Dijkstry
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print("Najkrótsze odległości od wierzchołka", start_vertex, "do innych wierzchołków:")
for vertex, distance in distances.items():
    print(f"Odległość do {vertex}: {distance}")
