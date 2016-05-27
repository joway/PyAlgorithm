import copy

from graph.Graph import Graph

'''
多源最短路
'''


class Floyd(Graph):
    def __init__(self, size=10):
        super().__init__(size=size)
        self.MAX = 100
        self.result = copy.deepcopy(self.graph)
        self.path = 0
        self.sorted()

    def sorted(self):
        for k in range(0, self.size):
            for i in range(0, self.size):
                for j in range(0, self.size):
                    if self.result[i][j] > 0 \
                            and self.result[i][k] + self.result[k][j] < self.result[i][j]:
                        self.result[i][j] = self.result[i][k] + self.result[k][j]
                        self.path = k

    def search(self, start, end):
        return self.result[start][end]

    def show_sorted(self):
        for i in self.result:
            print(i)
