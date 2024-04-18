class ListImplementationGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1]=[node2]

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} -> {'->'.join(map(str,self.graph[vertex]))}")


class AdjacencyMatrixImplementationGraph:
    def __init__(self, number_of_vertices):
        self.graph = [[0]*number_of_vertices for _ in range(number_of_vertices)]

    def add_edge(self, node1, node2):
        self.graph[node1][node2] = 1
        self.graph[node2][node1] = 1

    def print_graph(self):
        print(self.graph)


if __name__ == '__main__':
    g = ListImplementationGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 2)

    ag = AdjacencyMatrixImplementationGraph(5)
    ag.add_edge(0, 4)
    ag.add_edge(3, 4)
    ag.add_edge(2, 2)

    g.print_graph()
    ag.print_graph()