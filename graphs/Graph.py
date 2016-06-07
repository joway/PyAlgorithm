import random


class Graph(object):
    def __init__(self, size=10, graph=None):
        self.size = len(graph) if graph else size
        self.MAX = 100
        self.graph = graph or self.init_graph(self.size, self.MAX)

    @classmethod
    def init_graph(cls, size, infinity=1000):
        graph = []
        for i in range(0, size):
            row = []
            for t in range(0, size):
                if t == i:
                    # 0 代表环
                    row.append(0)
                elif random.random() > random.random():
                    row.append(int(random.random() * infinity / 10 + 1))
                else:
                    row.append(infinity)
            graph.append(row)
        return graph

    def show(self):
        for i in self.graph:
            print(i)
