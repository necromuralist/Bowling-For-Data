# python
from __future__ import annotations
from queue import Queue

# pypi
from attrs import define

# this project
from bowling.data_structures.graphs.graph import Graph, Vertex
from bowling.data_structures.graphs import graph


INFINITY = float("inf")


@define
class BreadthFirstSearch:
    """Creates a shortest-path tree from a source node to all reachable nodes

    Note:
     The vertices should be BFSVertex instances

    Args:
     graph: the graph with the adjacency dict for all the vertices
    """
    graph: Graph

    def __call__(self, source: BFSVertex) -> None:
        """Does the breadth first search to create the shortest paths tree"""
        # reset all the search attributes
        for vertex in set(self.graph.adjacent) - {source}:
            vertex.color, vertex.distance, vertex.predecessor = (
                graph.Color.WHITE, INFINITY, None)
    
        source.color, source.distance, source.predecessor = (
            graph.Color.GRAY, 0, None)
        queue = Queue()
        queue.put(source)
    
        while not queue.empty():
            predecessor = queue.get()
            for vertex in self.graph.adjacent[predecessor]:
                if vertex.color is graph.Color.WHITE:
                    vertex.color, vertex.distance, vertex.predecessor = (
                        graph.Color.GRAY, predecessor.distance + 1, predecessor)
                    queue.put(vertex)
            predecessor.color = graph.Color.BLACK
        return
