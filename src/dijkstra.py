# src/dijkstra.py

from graph import Graph
from priority_queue import PriorityQueue

def dijkstra(graph, start):
    """
    Implementacja algorytmu Dijkstry do znajdowania najkrótszych ścieżek z wierzchołka start.

    :param graph: Obiekt klasy Graph
    :param start: Wierzchołek startowy
    :return: Tuple (odległości, poprzednicy)
    """
    V = graph.V
    dist = [float('inf')] * V  # Inicjalizacja odległości
    prev = [None] * V  # Poprzednicy w najkrótszych ścieżkach
    dist[start] = 0  # Odległość do siebie samego wynosi 0

    # Inicjalizacja kolejki priorytetowej
    priority_queue = PriorityQueue()
    priority_queue.push(start, dist[start])

    while not priority_queue.is_empty():
        u, current_dist = priority_queue.pop()

        # Jeśli aktualna odległość jest większa niż zapisane, pomiń
        if current_dist > dist[u]:
            continue

        # Przeglądaj sąsiadów wierzchołka u
        for neighbor, weight in graph.adj[u]:
            alt = dist[u] + weight
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u
                priority_queue.push(neighbor, alt)

    return dist, prev

def reconstruct_path(prev, start, end):
    """
    Rekonstruuje najkrótszą ścieżkę z start do end.

    :param prev: Lista poprzedników
    :param start: Wierzchołek startowy
    :param end: Wierzchołek końcowy
    :return: Lista wierzchołków tworzących najkrótszą ścieżkę
    """
    path = []
    at = end
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()

    if path[0] == start:
        return path
    else:
        return []  # Brak ścieżki

if __name__ == "__main__":
    # Przykładowe użycie
    g = Graph(6)
    g.add_edge(0, 1, 7, directed=False)
    g.add_edge(0, 2, 9, directed=False)
    g.add_edge(0, 5, 14, directed=False)
    g.add_edge(1, 2, 10, directed=False)
    g.add_edge(1, 3, 15, directed=False)
    g.add_edge(2, 3, 11, directed=False)
    g.add_edge(2, 5, 2, directed=False)
    g.add_edge(3, 4, 6, directed=False)
    g.add_edge(4, 5, 9, directed=False)

    start_vertex = 0
    distances, predecessors = dijkstra(g, start_vertex)

    print(f"Najkrótsze odległości od wierzchołka {start_vertex}:")
    for vertex in range(g.V):
        print(f"Do wierzchołka {vertex}: {distances[vertex]}")

    end_vertex = 4
    path = reconstruct_path(predecessors, start_vertex, end_vertex)
    if path:
        print(f"\nNajkrótsza ścieżka z {start_vertex} do {end_vertex}: {' -> '.join(map(str, path))}")
    else:
        print(f"\nBrak ścieżki z {start_vertex} do {end_vertex}")
