import copy

from .graph import Graph

'''
单源最短路

一次性得到单个点到全部点的最短路径
'''


class Dijkstra(Graph):
    def __init__(self, size=10, graph=None):
        super().__init__(size=size, graph=graph)
        self.result = copy.deepcopy(self.graph)

    def shortest_path(self, start=None, end=None):
        S = {start: 0}
        # 初始化 U
        U = {v: self.graph[start][v] for v in range(0, self.size) if v != start}
        while len(S) < self.size:
            # min 函数的 key 参数传入一个函数
            # key函数返回的结果作为比较大小或排序的依据
            min_key = min(U, key=U.get)
            S[min_key] = U.get(min_key)
            U = {v: min(self.graph[min_key][v] + S[min_key],
                        U[v]) for v in U.keys() if v != min_key}
        return S.get(end or 0)
