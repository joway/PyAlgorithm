import copy

from .Graph import Graph

'''
多源最短路

时间复杂度为 {O(N^{3})} 空间复杂度为 { O(N^{2})} 。

一次性得到所有点的最短路径
'''


class Floyd(Graph):
    def __init__(self, size=10, graph=None):
        super().__init__(size=size, graph=graph)
        self.result = self.floyd_sort(self.graph)

    @classmethod
    def floyd_sort(cls, graph):
        size = len(graph)
        result = copy.deepcopy(graph)
        # k 为经过的点
        for k in range(0, size):
            for i in range(0, size):
                for j in range(0, size):
                    if i != j:
                        result[i][j] = min(result[i][j], result[i][k] + result[k][j])
        return result

    def shortest_path(self, start, end):
        return self.result[start][end]

    def show_sorted(self):
        for i in self.result:
            print(i)
