# Соединенный Граф
# Connected Graph

class Graph:
    __graph = {}

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

    def print(self):
        print(self.__graph)


def main():
    """
    Main function
    """

    print("-- Connected Graph --\n")

    edges = [(1, 2), (2, 3), (3, 1)]
    gr = Graph(edges)
    gr.print()
    gr.is_connected()


if __name__ == '__main__':
    main()
