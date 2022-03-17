# this project
from .node import Node
from .query import Query


class Tree:
    """Binary Search Tree

    Args:
     root: the root node for the tree
    """
    def __init__(self, root: Node=None) -> None:
        self.root = root
        self._query = None        
        return

    @property
    def query(self) -> Query:
        """A Tree Query"""
        if self._query is None:
            self._query = Query(self)
        return self._query

    def insert(self, node: Node) -> None:
        """Insert the node as a new leaf in the tree
    
        Args:
         node: a node to insert into the tree
        """
        hunter, hound = None, self.root
    
        while hound is not None:
            hunter, hound = hound, hound.left if node < hound else hound.right
    
        node.parent = hunter
    
        if hunter is None:
            self.root = node
        elif node.key < hunter.key:
            hunter.left = node
        else:
            hunter.right = node
        return

    def transplant(self, to_be_replaced: Node, replacement: Node) -> None:
        """Replace node with another
    
        Args:
         to_be_replaced: current holder of the position to be replaced
         replacement: node to replace the incumbent
        """
        if to_be_replaced.parent is None:
            self.root = replacement
        elif to_be_replaced == to_be_replaced.parent.left:
            to_be_replaced.parent.left = replacement
        else:
            to_be_replaced.parent.right = replacement
    
        if replacement is not None:
            replacement.parent = to_be_replaced.parent
        return

    def delete(self, node: Node) -> None:
        """Remove the node from the tree
    
        Args:
         node: node to remove from the tree
        """
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            replacement = self.query.min(node.right)
            if replacement.parent != node:
                self.transplant(replacement, replacement.right)
                replacement.right = node.right
                replacement.right.parent = replacement
            self.transplant(node, replacement)
            replacement.left = node.left
            replacement.left.parent = replacement
        return
