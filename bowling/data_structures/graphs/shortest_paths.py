# python
from __future__ import annotations
from dataclass import dataclass, field

INFINITE = INFINITY = float("inf")


@dataclass(order=True)
class Vertex:
    """A vertex for the single-source shortest paths problem

    Args:
     identifier: something to distinguish the vertex
     path_estimate: the estimate of the path weight
     predecessor: the vertex that precedes this one in the path
    """
    identifier: str=field(compare=False)
    path_estimate: float=INFINITE
    predecessor: Vertex=field(None, compare=False)

    def __repr__(self) -> str:
        return f"{self.identifier} (path-estimate={self.path_estimate})"


class Edge:
    """A directed edge

    Args:
     source: tail vertex of the edge
     target: head vertex of the edge
     weight: the weight of the edge
    """
    def __init__(self, source: Vertex, target: Vertex, weight: float) -> None:
        self.source = source
        self.target = target
        self.weight = weight
        return

    def __repr__(self) -> str:
        return f"{self.source} -- {self.weight} --> {self.target}"


class Graph:
    """Directed Graph for shortest path problem"""
    def __init__(self) -> None:
        self.vertices = set()
        self.edges = set()
        return

    def add_edge(self, edge: Edge) -> None:
        """Add the edge to the graph
    
        Args:
         edge: the directed edge to add
        """
        self.edges.add(edge)
        self.vertices.add(edge.source)
        self.vertices.add(edge.target)
        return


def initialize_single_source(graph: Graph, source: Vertex) -> None:
    """Setup the vertices of the graphs for single-source shortest path

    Args:
     graph: graph with vertices to set up
     source: the vertex to use as the start of the shortest paths tree
    """
    for vertex in graph.vertices:
        vertex.path_estimate = INFINITY
        vertex.predecessor = None
    source.path_estimate = 0
    return


def relax(edge: Edge) -> None:
    """Check if target Vertex is improved using the source vertex

    Args:
     edge: directed edge with source, target, and weight
    """
    if edge.target.path_estimate > edge.source.path_estimate + edge.weight:
        edge.target.path_estimate = edge.source.path_estimate + edge.weight
        edge.target.predecessor = edge.source
    return
