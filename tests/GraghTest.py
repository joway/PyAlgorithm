from graph.Dijkstra import Dijkstra
from graph.Floyd import Floyd
from graph.Graph import Graph
from tests.GeneralTestCase import GeneralTestCase


class GraphTest(GeneralTestCase):
    def setUp(self):
        super().setUp()
        # self.graph = [[1000, 1, 2, 1000],
        #               [5, 1000, 2, 1000],
        #               [1000, 8, 1000, 2],
        #               [2, 8, 3, 1000]]
        self.graph = Graph.init_graph(100)

    def test_graph(self):
        floyd = Floyd(graph=self.graph)
        dijkstra = Dijkstra(graph=self.graph)
        self.assertEqual(floyd.shortest_path(0, 1), dijkstra.shortest_path(0, 1))


        # def test_dijkstra(self):
        #     print(self.graph)
        #     dijkstra = Dijkstra(graph=self.graph)
        #     print(dijkstra.shortest_path(0, 1))
