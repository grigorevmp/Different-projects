# Соединенный Граф
# Connected Graph

class Graph:
    __graph = {}
    __matrix = []

    def __init__(self, edges):
        for edge in edges:
            if len(edge) == 1:
                edge = (edge[0], None)
            if edge[0] in self.__graph:
                if not edge[1] in self.__graph:
                    self.__graph[edge[1]] = [None]
                if not edge[1] in self.__graph[edge[0]]:
                    self.__graph[edge[0]].append(edge[1])
            else:
                self.__graph[edge[0]] = [edge[1]]
                if not edge[1] in self.__graph:
                    self.__graph[edge[1]] = [None]

    def is_connected(self):
        start_node = list(self.__graph.keys())[0]
        color = {v: 'white' for v in self.__graph.keys()}
        color[start_node] = 'gray'
        S = [start_node]
        while len(S) != 0:
            u = S.pop()
            for v in self.__graph[u]:
                if v:
                    if color[v] == 'white':
                        color[v] = 'gray'
                        S.append(v)
                    color[u] = 'black'
        print(list(color.values()).count('black') == len(self.__graph.keys()))

    def createMatrix(self):
        infinity = 1000000
        self.__matrix = []
        n = len(self.__graph.keys())
        for i in range(n):
            self.__matrix.append([infinity] * n)
        for u in self.__graph.keys():
            for v in self.__graph[u]:
                if v:
                    self.__matrix[u - 1][v - 1] = 1

    def dijkstra(self):
        matrix = self.__matrix
        N = len(self.__graph.keys())
        S = 1
        valid = [True] * N
        weight = [1000000] * N
        weight[S] = 0
        for i in range(N):
            min_weight = 1000001
            ID_min_weight = -1
            for j in range(N):
                if valid[j] and weight[j] < min_weight:
                    min_weight = weight[j]
                    ID_min_weight = j
            for z in range(N):
                if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
                    weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]
            valid[ID_min_weight] = False
        print(weight)

    def print(self):
        print(self.__graph)


def main():
    """
    Main function
    """

    print("-- Dijkstra --\n")

    edges = [(1, 2), (2, 3), (3, 1)]
    gr = Graph(edges)
    gr.print()
    gr.is_connected()
    gr.createMatrix()
    gr.dijkstra()


if __name__ == '__main__':
    main()
