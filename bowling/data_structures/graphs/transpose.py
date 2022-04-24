# python
from collections import defaultdict

# this project
from bowling.data_structures.graphs.depth_first_search import (
    DepthFirstSearch,
    DFSVertex,
    DirectedGraph)


class Transpose:
    """Creates the transpose of a graph

    Args:
     graph: the directed graph to transpose
    """
    def __init__(self, graph: DirectedGraph) -> None:
        self.graph = graph
        self._adjacent = None
        self._vertices = None
        return

    @property
    def adjacent(self) -> dict:
        """Vertex: set of adjacente vertices dictionary"""
        if self._adjacent is None:
            self._adjacent = defaultdict(set)
            
            for vertex, neighbors in self.graph.adjacent.items():
                for neighbor in neighbors:
                    print(f"Adding neighbor {vertex} to {self.vertices}")
                    self._adjacent[neighbor].add(vertex)
        return self._adjacent

    @property
    def vertices(self) -> set:
        """The vertices in the directed graph"""
        if self._vertices is None:
            self._vertices = self.graph.vertices
        return self._vertices

    


class StronglyConnectedComponents:
    """Build the strongly connected components sub-trees

    Args:
     graph: directed graph to process
    """
    def __init__(self, graph: DirectedGraph) -> None:
        self.graph = graph
        self._transpose = None
        self._forest = None
        return

    @property
    def transpose(self) -> Transpose:
        """The transpose of the original graph"""
        if self._transpose is None:
            self._transpose = Transpose(self.graph)
        return self._transpose

    def find_child(self, vertices: set, predecessor: DFSVertex,
                   path: list) -> list:
        """Find the child nodes of the given predecessor
    
        Note:
         this is a helper to find the children in a Strongly Connected Component
         For it to make sense the vertices should have the forest already built
    
        Args:
         vertices: source of nodes
         predecessor: node in the graph to find the child of
         path: list to append child nodes to
        """
        for vertex in vertices:
            if vertex.predecessor is predecessor:
                path.append(vertex)
                self.find_child(vertices, vertex, path)
        return path

    @property
    def forest(self) -> dict:
        """creates the forest with the strongly connected components
    
        Returns:
         adjacency dict for the strongly connected components
        """
        if self._forest is None:
            # do the search to get the finish times
            searcher = DepthFirstSearch(self.graph)
            searcher()
    
            # change the transpose vertices to be in reversed finish order
            vertices = sorted(self.graph.vertices,
                              key=lambda vertex: vertex.finished,
                              reverse=True)
            self.transpose._vertices = dict(zip(vertices, (None,) * len(vertices)))
    
            # do a depth first search on the graph transpose
            searcher.graph = self.transpose
            searcher()
    
            # at this point the strongly connected components are set up in 
            # self.transpose, but you have to do some figuring to get the trees
    
            # get the roots of the trees in the forest
            roots = (vertex for vertex in self.transpose.vertices
                     if vertex.predecessor is None)
    
            # build a forest for each root by finding its children
            forest = (self.find_child(self.transpose.vertices, root, [root])
                      for root in roots)
    
            # build a new adjacency dict
            self._forest = dict()
    
            # the neighbors are all the original adjacent nodes without the 
            # tree nodes
            for tree in forest:
                neighbors = set()
                for node in tree:
                    neighbors = neighbors.union(self.graph.adjacent[node])
                neighbors = neighbors - set(tree)
                self._forest[tuple(tree)] = neighbors
        return self._forest
