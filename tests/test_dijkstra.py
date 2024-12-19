# tests/test_dijkstra.py

import unittest
from src.dijkstra import dijkstra, reconstruct_path
from src.graph import Graph

class TestDijkstra(unittest.TestCase):
    def test_shortest_path_undirected(self):
        g = Graph(5)
        g.add_edge(0, 1, 10, directed=False)
        g.add_edge(0, 2, 3, directed=False)
        g.add_edge(1, 2, 1, directed=False)
        g.add_edge(1, 3, 2, directed=False)
        g.add_edge(2, 1, 4, directed=False)
        g.add_edge(2, 3, 8, directed=False)
        g.add_edge(2, 4, 2, directed=False)
        g.add_edge(3, 4, 7, directed=False)
        g.add_edge(4, 3, 9, directed=False)

        distances, predecessors = dijkstra(g, 0)
        path = reconstruct_path(predecessors, 0, 3)
        self.assertEqual(path, [0, 2, 1, 3])

    def test_no_path(self):
        g = Graph(3)
        g.add_edge(0, 1, 5, directed=True)
        # Nie dodajemy krawędzi z 1 do 2, więc nie ma ścieżki z 0 do 2
        distances, predecessors = dijkstra(g, 0)
        path = reconstruct_path(predecessors, 0, 2)
        self.assertEqual(path, [])

    def test_single_vertex(self):
        g = Graph(1)
        distances, predecessors = dijkstra(g, 0)
        self.assertEqual(distances, [0])
        self.assertEqual(predecessors, [None])

if __name__ == '__main__':
    unittest.main()
