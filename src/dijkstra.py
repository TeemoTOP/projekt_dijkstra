# src/dijkstra.py
import sys
import os
import matplotlib.pyplot as plt
import networkx as nx


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.graph import Graph
from src.priority_queue import PriorityQueue

def dijkstra(graph, start):
    """
    Implementacja algorytmu Dijkstry do znajdowania najkrótszych ścieżek z wierzchołka start.

    Algorytm:
    - Dla każdego wierzchołka inicjalizujemy najkrótszą odległość jako nieskończoność,
      oprócz wierzchołka początkowego, dla którego odległość wynosi 0.
    - Używamy kolejki priorytetowej, aby zawsze wybierać wierzchołek z najmniejszym kosztem.
    - Dla każdego sąsiada aktualizujemy odległości, jeśli znaleziono krótszą ścieżkę.

    Ograniczenia:
    - Algorytm działa wyłącznie z grafami o nieujemnych wagach krawędzi.

    :param graph: Obiekt klasy Graph reprezentujący graf.
    :param start: Wierzchołek początkowy, od którego liczymy najkrótsze ścieżki.
    :return: Tuple (odległości, poprzednicy).
        - odległości: Lista minimalnych odległości od wierzchołka startowego.
        - poprzednicy: Lista poprzedników dla każdego wierzchołka na najkrótszej ścieżce.
    """
    if graph.V == 0:
        raise ValueError("Graf nie może być pusty.")
    if start < 0 or start >= graph.V:
        raise ValueError(f"Wierzchołek startowy {start} jest poza zakresem.")

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
    
def visualize_graph(graph, path, title="Graph Visualization"):
    """
    Wizualizuje graf i podświetla najkrótszą ścieżkę.

    :param graph: Obiekt klasy Graph.
    :param path: Najkrótsza ścieżka (lista wierzchołków).
    :param title: Tytuł grafu.
    """
    G = nx.Graph()

    # Dodaj krawędzie do grafu NetworkX
    for u in range(graph.V):
        for v, weight in graph.adj[u]:
            G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G)  # Układ wierzchołków
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Podświetlenie najkrótszej ścieżki
    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title(title)
    plt.show()

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
        visualize_graph(g, path, title=f"Najkrótsza ścieżka z {start_vertex} do {end_vertex}")
    else:
        print(f"\nBrak ścieżki z {start_vertex} do {end_vertex}")
        visualize_graph(g, [], title="Graf bez ścieżki")
