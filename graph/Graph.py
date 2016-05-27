import random


class Graph(object):
    def __init__(self, size=10):
        graph = []
        self.size = size
        self.MAX = 100
        for i in range(0, self.size):
            row = []
            for t in range(0, self.size):
                if t == i:
                    row.append(0)
                elif random.random() > 0.5:
                    row.append(int(random.random() * 5 + 1))
                else:
                    row.append(self.MAX)

            graph.append(row)
        self.graph = graph

    def show(self):
        for i in self.graph:
            print(i)


