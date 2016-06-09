from datastructure.graphs.dijkstra import Dijkstra
from datastructure.graphs.floyd import Floyd
from datastructure.graphs.graph import Graph
from tests.base_test_case import BaseTestCase


class GraphTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        # self.graphs = [[1000, 1, 2, 1000],
        #               [5, 1000, 2, 1000],
        #               [1000, 8, 1000, 2],
        #               [2, 8, 3, 1000]]
        self.graph = Graph.init_graph(100)

    def test_graph(self):
        floyd = Floyd(graph=self.graph)
        dijkstra = Dijkstra(graph=self.graph)
        self.assertEqual(floyd.shortest_path(0, 1), dijkstra.shortest_path(0, 1))
