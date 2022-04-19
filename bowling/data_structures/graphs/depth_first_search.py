# python
from __future__ import annotations
from enum import Enum

# from pypi
from attrs import define

# this projects
from bowling.data_structures.graphs import graph





@define(eq=False)
class DFSVertex(graph.Vertex):
    """The Depth-First Search Vertex

    Args:
     identifier: something to identify the node
     color: the 'discovery' state of the node
     distance: The number of edges to the root
     predecessor: The 'parent' of the node in a tree
     discovered: when the node was discovered
     finished: when the node's adjacent nodes where checked
    """
    discovered: int = None
    finished: int = None
    def __str__(self) -> str:
        return (super().__str__() + 
        f", discovered: {self.discovered}, finished: {self.finished}")


class DirectedGraph(graph.Graph):
    """A Directed Graph"""    

    def add(self, source: DFSVertex, target: DFSVertex) -> None:
        """Add an edge from source to target
    
        Args:
         source: the vertex where the edge starts
         target: the vertex where the edge ends
        """
        self.vertices.add(source)
        self.vertices.add(target)
        self.adjacent[source].add(target)
        return


@define
class DepthFirstSearch:
    """depth-first-searcher

    Args:
     graph: the graph to process
    """
    graph: graph.Graph
    time: int=0

    def __call__(self) -> None:
        """Performs the depth-first-search"""
        for vertex in self.graph.vertices:
            vertex.color = graph.Color.WHITE
            vertex.predecessor = None
        self.time = 0
        for vertex in self.graph.vertices:
            if vertex.color is graph.Color.WHITE:
                self.visit_adjacent(vertex)
        return

    def visit_adjacent(self, vertex: DFSVertex) -> None:
        """Visit the nodes adjacent to the given node
    
        Args:
         vertex: vertex whose adjacency to visit
        """
        self.time += 1
        vertex.discovered = self.time
        vertex.color = graph.Color.GRAY
        for neighbor in self.graph.adjacent[vertex]:
            if neighbor.color is graph.Color.WHITE:
                neighbor.predecessor = vertex
                self.visit_adjacent(neighbor)
        vertex.color = graph.Color.BLACK
        self.time += 1
        vertex.finished = self.time
        return
