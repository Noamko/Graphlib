from typing import Iterable, Tuple
from abc import ABC, abstractmethod

class Graph(ABC):
    def __init__(self, nodes: Iterable=None, edges: Iterable=None) -> None:
        self.nodes = []
        self.edges = []
        self.neighbors_list = {}
        self.matrix = [[float("inf") for _ in range(len(nodes))] for _ in range(len(nodes))]
        if nodes != None:
            for n in nodes:
                node = self.Node(n)
                self.nodes.append(node)
                self.neighbors_list[node] = []
            
        if edges != None:
            for e in edges:
                self.edges.append(self.Edge(e))
    
    def print_matrix(self):
        print(self.matrix)

    def get_neighbors(self, node):
        if node in self.nodes:
            return self.neighbors_list[node]

    class Node:
        def __init__(self, node) -> None:
            self.value = node

        def __repr__(self) -> str:
            return str(self.value)

        def __eq__(self, __o: object) -> bool:
            return self.value == __o

        def __hash__(self) -> int:
            return self.value.__hash__()
        
        def __str__(self) -> str:
            return  f"({str(self.value)})"
        

    class Edge:
        def __init__(self, a, b, cost=1) -> None:
            self.value = (Graph.Node(a), Graph.Node(b))
            self.cost = cost

        def __init__(self, tpl: Tuple, cost=1) -> None:
            self.value = (Graph.Node(tpl[0]), Graph.Node(tpl[1]))
            self.cost = cost

        def __eq__(self, __o: object) -> bool:
            return self.value == __o

        def __hash__(self) -> int:
            return self.value.__hash__()

class UnDirectedGraph(Graph):
    def __init__(self, nodes: Iterable=None, edges: Iterable=None) -> None:
        super().__init__(nodes, edges)
        for e in self.edges:
            a, b = e.value
            self.matrix[self.nodes.index(a)][self.nodes.index(b)] = e.cost
            self.matrix[self.nodes.index(b)][self.nodes.index(a)] = e.cost

            if a in self.neighbors_list:
                if b not in self.neighbors_list[a]: self.neighbors_list[a].append(b)
            else: self.neighbors_list[a] = [b]

            if b in self.neighbors_list:
                if a not in self.neighbors_list[b]: self.neighbors_list[b].append(a)
            else: self.neighbors_list[b] = [a]
    
    def __str__(self) -> str:
        res = ""
        for e in self.edges:
            a, b = e.value
            res += f"{a}--{e.cost}--{b}\n"
        return res
    def __repr__(self) -> str:
        res = ""
        for e in self.edges:
            a, b = e.value
            res += f"{a} --{e.cost}--{b}\n"
        return res


class DirectedGraph(Graph):
    def __init__(self, nodes: Iterable=None, edges: Iterable=None) -> None:
        super().__init__(nodes, edges)
        for e in self.edges:
            a, b = e.value
            self.matrix[self.nodes.index(a)][self.nodes.index(b)] = e.cost

            if a in self.neighbors_list:
                if b not in self.neighbors_list[a]: self.neighbors_list[a].append(b)
            else: self.neighbors_list[a] = [b]
    
    def __str__(self) -> str:
        res = ""
        for e in self.edges:
            a, b = e.value
            res += f"{a}--{e.cost}-->{b}\n"
        return res

    def __repr__(self) -> str:
        res = ""
        for e in self.edges:
            a, b = e.value
            res += f"{a}--{e.cost}-->{b}\n"
        return res


nodes = [1,2,3,4]
edges = [(1,2), (1,3), (4,3)]
g = DirectedGraph(nodes, edges)
print(g.get_neighbors(1))
print(g)