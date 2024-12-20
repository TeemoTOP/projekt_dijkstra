import unittest
from src.dijkstra import dijkstra, reconstruct_path
from src.graph import Graph

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        # Setup a default graph for reuse in multiple tests
        print(f"Starting test: {self._testMethodName}")
        self.graph = Graph(5)
        self.graph.add_edge(0, 1, 10, directed=False)
        self.graph.add_edge(0, 2, 3, directed=False)
        self.graph.add_edge(1, 2, 1, directed=False)
        self.graph.add_edge(1, 3, 2, directed=False)

    def tearDown(self):
        # Clear the graph after each test
        print(f"Finished test: {self._testMethodName}")
        self.graph = None

    def test_dijkstra_distances(self):
        """Tests the distance calculation of the Dijkstra algorithm."""
        distances, _ = dijkstra(self.graph, 0)
        print(f"Distances from source: {distances}")
        self.assertEqual(distances[3], 6, "Incorrect distance to vertex 3")

    def test_reconstruct_path(self):
        """Tests the path reconstruction using predecessors."""
        _, predecessors = dijkstra(self.graph, 0)
        path = reconstruct_path(predecessors, 0, 3)
        print(f"Path reconstructed: {path}")
        self.assertEqual(path, [0, 2, 1, 3], "Incorrect path reconstruction")

    def test_no_path(self):
        """Tests the case where no path exists between nodes."""
        g = Graph(3)
        g.add_edge(0, 1, 5, directed=True)
        distances, predecessors = dijkstra(g, 0)
        path = reconstruct_path(predecessors, 0, 2)
        print(f"Distances: {distances}, Path: {path}")
        self.assertEqual(path, [], "Path should be empty for unconnected nodes")

    def test_single_vertex(self):
        """Tests a graph with a single vertex."""
        g = Graph(1)
        distances, predecessors = dijkstra(g, 0)
        print(f"Distances: {distances}, Predecessors: {predecessors}")
        self.assertEqual(distances, [0], "Distance to itself should be 0")
        self.assertEqual(predecessors, [None], "Predecessor should be None")

    def test_graph_with_edges(self):
        """Tests the algorithm with a simple graph setup."""
        g = Graph(3)
        g.add_edge(0, 1, 5, directed=False)
        g.add_edge(1, 2, 10, directed=False)
        distances, predecessors = dijkstra(g, 0)
        print(f"Distances: {distances}")
        self.assertEqual(distances[2], 15, "Incorrect distance to vertex 2")
        path = reconstruct_path(predecessors, 0, 2)
        print(f"Path reconstructed: {path}")
        self.assertEqual(path, [0, 1, 2], "Incorrect path to vertex 2")

    def test_multiple_graphs(self):
        """Tests the algorithm on multiple graph configurations."""
        test_cases = [
            (Graph(3), [(0, 1, 5)], 0, 2, []),  # No path
            (Graph(5), [(0, 1, 10), (0, 2, 3)], 0, 2, [0, 2])  # Path [0, 2]
        ]
        for g, edges, start, end, expected in test_cases:
            with self.subTest(graph=g, start=start, end=end):
                for u, v, w in edges:
                    g.add_edge(u, v, w, directed=False)
                distances, predecessors = dijkstra(g, start)
                path = reconstruct_path(predecessors, start, end)
                print(f"Graph: {g}, Start: {start}, End: {end}, Distances: {distances}, Path: {path}")
                self.assertEqual(path, expected, f"Unexpected path for graph from {start} to {end}")

if __name__ == '__main__':
    unittest.main()
