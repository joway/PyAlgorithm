from .graph import Graph

'''
'''


class DFS(Graph):
    def __init__(self, size=10, graph=None):
        super().__init__(size=size, graph=graph)

    @classmethod
    def dsf(cls, graph):
        pass