# src/graph.py

class Graph:
    def __init__(self, vertices):
        """
        Inicjalizuje graf.

        :param vertices: Liczba wierzchołków w grafie
        """
        self.V = vertices  # Liczba wierzchołków
        self.adj = [[] for _ in range(vertices)]  # Lista sąsiedztwa

    def add_edge(self, u, v, weight, directed=True):
        """
        Dodaje krawędź do grafu.

        :param u: Wierzchołek początkowy.
        :param v: Wierzchołek końcowy.
        :param weight: Waga krawędzi. Musi być nieujemna.
        :param directed: Czy graf jest skierowany.
        :raises ValueError: Jeśli waga krawędzi jest ujemna.
        """
        if weight < 0:
            raise ValueError("Waga krawędzi nie może być ujemna.")
        
        self.adj[u].append((v, weight))
        if not directed:
            self.adj[v].append((u, weight))

