import unittest
from src.dijkstra import dijkstra, reconstruct_path
from src.graph import Graph

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        # Ustawienie domyślnego grafu do ponownego wykorzystania w wielu testach
        print(f"\nRozpoczynanie testu: {self._testMethodName}")
        self.graph = Graph(5)
        self.graph.add_edge(0, 1, 10, directed=False)
        self.graph.add_edge(0, 2, 3, directed=False)
        self.graph.add_edge(1, 2, 1, directed=False)
        self.graph.add_edge(1, 3, 2, directed=False)

    def tearDown(self):
        # Czyszczenie grafu po każdym teście
        print(f"Zakończenie testu: {self._testMethodName}")
        self.graph = None

    def test_dijkstra_distances(self):
        """Test obliczania odległości za pomocą algorytmu Dijkstry."""
        distances, _ = dijkstra(self.graph, 0)
        print(f"Odległości od źródła: {distances}")
        self.assertEqual(distances[3], 6, "Nieprawidłowa odległość do wierzchołka 3")

    def test_reconstruct_path(self):
        """Test rekonstrukcji ścieżki za pomocą poprzedników."""
        _, predecessors = dijkstra(self.graph, 0)
        path = reconstruct_path(predecessors, 0, 3)
        print(f"Zrekonstruowana ścieżka: {path}")
        self.assertEqual(path, [0, 2, 1, 3], "Nieprawidłowa rekonstrukcja ścieżki")

    def test_no_path(self):
        """Test przypadku, gdy brak ścieżki między wierzchołkami."""
        g = Graph(3)
        g.add_edge(0, 1, 5, directed=True)
        distances, predecessors = dijkstra(g, 0)
        path = reconstruct_path(predecessors, 0, 2)
        print(f"Odległości: {distances}, Ścieżka: {path}")
        self.assertEqual(path, [], "Ścieżka powinna być pusta dla niepołączonych wierzchołków")

    def test_single_vertex(self):
        """Test grafu z pojedynczym wierzchołkiem."""
        g = Graph(1)
        distances, predecessors = dijkstra(g, 0)
        print(f"Odległości: {distances}, Poprzednicy: {predecessors}")
        self.assertEqual(distances, [0], "Odległość do samego siebie powinna wynosić 0")
        self.assertEqual(predecessors, [None], "Poprzednik powinien być None")

    def test_graph_with_edges(self):
        """Test algorytmu na prostym grafie z krawędziami."""
        g = Graph(3)
        g.add_edge(0, 1, 5, directed=False)
        g.add_edge(1, 2, 10, directed=False)
        distances, predecessors = dijkstra(g, 0)
        print(f"Odległości: {distances}")
        self.assertEqual(distances[2], 15, "Nieprawidłowa odległość do wierzchołka 2")
        path = reconstruct_path(predecessors, 0, 2)
        print(f"Zrekonstruowana ścieżka: {path}")
        self.assertEqual(path, [0, 1, 2], "Nieprawidłowa ścieżka do wierzchołka 2")

    def test_multiple_graphs(self):
        """Test algorytmu na różnych konfiguracjach grafu."""
        test_cases = [
            (Graph(3), [(0, 1, 5)], 0, 2, []),  # Brak ścieżki
            (Graph(5), [(0, 1, 10), (0, 2, 3)], 0, 2, [0, 2])  # Ścieżka [0, 2]
        ]
        for g, edges, start, end, expected in test_cases:
            with self.subTest(graph=g, start=start, end=end):
                for u, v, w in edges:
                    g.add_edge(u, v, w, directed=False)
                distances, predecessors = dijkstra(g, start)
                path = reconstruct_path(predecessors, start, end)
                print(f"Graf: {g}, Start: {start}, Koniec: {end}, Odległości: {distances}, Ścieżka: {path}")
                self.assertEqual(path, expected, f"Nieoczekiwana ścieżka dla grafu od {start} do {end}")

    def test_large_graph(self):
        """Test algorytmu Dijkstry na dużym grafie."""
        num_vertices = 1000
        g = Graph(num_vertices)

        # Dodaj krawędzie z wagami i modulo 10
        for i in range(num_vertices - 1):
            g.add_edge(i, i + 1, i % 10 + 1, directed=False)
        
        print(f"Liczba wierzchołków: {g.V}")
        print(f"Przykładowe krawędzie: {g.adj[:5]}")  # Wyświetlenie kilku pierwszych krawędzi
        
        distances, predecessors = dijkstra(g, 0)

        # Oblicz oczekiwaną odległość
        expected_distance = sum(i % 10 + 1 for i in range(num_vertices - 1))
        print(f"Odległości do ostatniego wierzchołka: {distances[num_vertices - 1]}")
        print(f"Oczekiwana odległość: {expected_distance}")

        self.assertEqual(distances[num_vertices - 1], expected_distance,
                        f"Nieprawidłowa odległość dla dużego grafu. Oczekiwano {expected_distance}, otrzymano {distances[num_vertices - 1]}")


if __name__ == '__main__':
    unittest.main()
