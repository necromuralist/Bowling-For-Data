# python
from __future__ import annotations
from collections import defaultdict
from enum import Enum


class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3

INFINITY = float("inf")


class Vertex:
    """A single node in a graph

    Args:
     identifier: something to identify the node
     color: the 'discovery' state of the node
     distance: The number of edges to the root
     predecessor: The 'parent' of the node in a tree
    """
    def __init__(self, identifier, color: Enum=Color.WHITE,
                 distance: float=INFINITY,
                 predecessor: Vertex=None) -> None:
        self.identifier = identifier
        self.color = color
        self.distance = distance
        self.predecessor = predecessor
        return

    def __str__(self) -> str:
        return (f"{self.identifier}: {self.color}, "
                f"distance: {self.distance}, predecessor: {self.predecessor}")


class Graph:
    """A graph implementation

    """
    def __init__(self) -> None:
        self._adjacent = None
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

    def add(self, node_1: Vertex, node_2: Vertex) -> None:
        """Add (bidirectional) edge
    
        Args:
         node_1: node on one end of the edge
         node_2: Node on the other end of the edge
        """
        self.adjacent[node_1].add(node_2)
        self.adjacent[node_2].add(node_1)
        return

    def __getitem__(self, key):
        """Get the list from the adjacencies dict
        
        Args:
         key: vertex whose list we want
        """
        return self.adjacent[key]
