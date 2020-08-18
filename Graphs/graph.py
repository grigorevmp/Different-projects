# Граф
# Graph

class Graph:
    __vertexes = []
    __edges = []

    """
    edge - [(vertex, vertex), weight]
    """

    def __init__(self, vertexes=None, edges=None):
        """
        :param vertexes:
        :param edges:
        """
        self.__matrix = []
        if edges is None:
            edges = []
        if vertexes is None:
            vertexes = []
        self.__edges = edges
        self.__vertexes = vertexes

    def isConnected(self):
        startNode = list(self.__vertexes)[0]
        color = {v: 'white' for v in self.__vertexes}
        color[startNode] = 'gray'
        S = [startNode]
        while len(S) != 0:
            u = S.pop()
            for V in self.__edges:
                if V[0][0] == u:
                    v = V[0][1]
                    if color[v] == 'white':
                        color[v] = 'gray'
                        S.append(v)
                    color[u] = 'black'
        return list(color.values()).count('black') == len(self.__vertexes)

    def createMatrix(self):
        infinity = 1000000
        n = len(self.__vertexes)
        for i in range(n):
            self.__matrix.append([infinity] * n)
        for V in self.__edges:
            u = V[0][0]
            v = V[0][1]
            w = V[1]
            self.__matrix[u-1][v-1] = w

    def isEulerian(self):
        if not self.isConnected():
            return "not eulerian "
        else:
            odd = 0
            for u in self.__vertexes:
                _sum = 0
                for V in self.__edges:
                    if V[0][0] == u:
                        _sum += 1
                if _sum % 2 != 0:
                    odd += 1

            if odd == 0:
                return "eulerian"
            elif odd == 2:
                return "semi-eulerian"
            elif odd > 2:
                return "not eulerian "

    def dijkstra(self, S):
        S -= 1
        if self.__matrix is None:
            self.createMatrix()
        N = len(self.__vertexes)
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
                if weight[ID_min_weight] + self.__matrix[ID_min_weight][z] < weight[z]:
                    weight[z] = weight[ID_min_weight] + self.__matrix[ID_min_weight][z]
            valid[ID_min_weight] = False
        print(weight)

    def addEdge(self, edge):
        """
        :param edge: - new Edge
        """
        try:
            vertex1 = edge[0][0]
            vertex2 = edge[0][1]
            if vertex1 not in self.__vertexes:
                self.addVertex(vertex1)
            if vertex2 not in self.__vertexes:
                self.addVertex(vertex2)
            self.__edges.append(edge)
        except ValueError:
            print("Wrong data")

    def delEdge(self, edge):
        """
        :param edge: - new Edge
        """
        for _edge in self.__edges:
            if edge == _edge:
                del _edge

    def addVertex(self, vertex):
        """
        :param vertex: - new Vertex
        """
        self.__vertexes.append(vertex)

    def delVertex(self, vertex):
        """
        :param vertex: - Vertex for deleting
        """
        del self.__vertexes[vertex]
        for edge in self.__edges:
            if vertex in edge:
                del edge

    def showVertexes(self):
        """
        :return: - Show vertexes
        """
        print("Vertexes: ", self.__vertexes)

    def showEdges(self):
        """
        :return: - Show edges
        """
        for edge in self.__edges:
            print("Edge: ", edge[0], " weight:", edge[1])


def main():
    """
    Main function
    """

    print("-- Graph --\n")

    gr = Graph()
    gr.addVertex(1)
    gr.addVertex(2)
    gr.addEdge([(1, 2), 1])
    gr.addEdge([(2, 1), 1])
    gr.addEdge([(3, 4), 1])
    gr.addEdge([(4, 3), 1])
    gr.addEdge([(3, 1), 1])
    gr.addEdge([(1, 3), 1])
    gr.addEdge([(3, 2), 1])
    gr.addEdge([(2, 3), 1])
    gr.addEdge([(4, 2), 1])
    gr.addEdge([(2, 4), 1])
    gr.addEdge([(4, 1), 5])
    gr.addEdge([(1, 4), 5])
    gr.showVertexes()
    gr.showEdges()
    print("Is connected: ", gr.isConnected())
    gr.createMatrix()
    gr.dijkstra(1)
    print(f"Is Eulerian: {gr.isEulerian()}")


if __name__ == '__main__':
    main()
