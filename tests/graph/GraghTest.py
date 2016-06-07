from graphs.Dijkstra import Dijkstra
from graphs.Floyd import Floyd
from graphs.Graph import Graph
from tests.GeneralTestCase import GeneralTestCase


class GraphTest(GeneralTestCase):
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


        # def test_dijkstra(self):
        #     print(self.graphs)
        #     dijkstra = Dijkstra(graphs=self.graphs)
        #     print(dijkstra.shortest_path(0, 1))
