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

    def isConnected(self):
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

    def isEulerian(self):
        # Check if all non-zero degree vertices are connected
        if not self.isConnected():
            return 0
        else:
            # Count vertices with odd degree
            odd = 0
            for u in self.__graph.keys():
                if len(self.__graph[u]) % 2 != 0:
                    odd += 1

            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0

    def print(self):
        print(self.__graph)


def main():
    """
    Main function
    """

    print("-- Eulerian --\n")

    edges = [(1, 2), (2, 3), (3, 1)]
    gr = Graph(edges)
    gr.print()
    gr.isConnected()
    gr.isEulerian()


if __name__ == '__main__':
    main()
