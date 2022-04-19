# python
from __future__ import annotations
from collections import defaultdict
from enum import Enum

# pypi
from attrs import define


class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3

INFINITY = float("inf")


@define(eq=False)
class Vertex:
    """A single node in a graph

    Args:
     identifier: something to identify the node
     color: the 'discovery' state of the node
     distance: The number of edges to the root
     predecessor: The 'parent' of the node in a tree
    """
    identifier: int
    color: Enum=Color.WHITE
    distance: float=INFINITY
    predecessor: Vertex=None
    
    def __str__(self) -> str:
        return (f"{self.identifier}: {self.color}, "
                f"distance: {self.distance}, predecessor: {self.predecessor}")


class Graph:
    """A graph implementation

    """
    def __init__(self) -> None:
        self._adjacent = None
        self._vertices = None
        return

    @property
    def adjacent(self) -> defaultdict:
        """The dictionary of adjacent vertices"""
        if self._adjacent is None:
            self._adjacent = defaultdict(set)
        return self._adjacent
    
    @adjacent.setter
    def adjacent(self, new_adjacent: dict) -> None:
        """Sets the dictionary of adjacent vertices (converting to default dict)
    
        Note:
         This expects the new_adjacent to be a dict of node: set of nodes
        """
        if type(new_adjacent) is not defaultdict:
            new_new_adjacent = defaultdict(set)
            for key, nodes in new_adjacent.items():
                new_new_adjacent[key] = nodes
            new_adjacent = new_new_adjacent
        self._adjacent = new_adjacent
        return

    @property
    def vertices(self) -> set:
        """The vertices in this graph"""
        if self._vertices is None:
            self._vertices = set()
        return self._vertices

    def add(self, node_1: Vertex, node_2: Vertex) -> None:
        """Add edge 
    
        Warning:
         This assumes an undirected graph, change it for a directed graph
    
        Args:
         node_1: node on one end of the edge
         node_2: Node on the other end of the edge
        """
        self.vertices.add(node_1)
        self.vertices.add(node_2)
        self.adjacent[node_1].add(node_2)
        self.adjacent[node_2].add(node_1)
        return

    def __getitem__(self, key):
        """Get the list from the adjacencies dict
        
        Args:
         key: vertex whose list we want
        """
        return self.adjacent[key]
