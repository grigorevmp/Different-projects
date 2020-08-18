# Граф
# Graph

class Graph:
    __graph = {}

    def __init__(self, edges):
        for edge in edges:
            if edge[0] in self.__graph:
                self.__graph[edge[0]].append(edge[1])
            else:
                self.__graph[edge[0]] = [edge[1]]

    def print(self):
        print(self.__graph)


def main():
    """
    Main function
    """

    print("-- Graph --\n")

    edges = [(1, 2), (1, 4), (2, 3), (3, 4)]
    gr = Graph(edges)
    gr.print()


if __name__ == '__main__':
    main()
