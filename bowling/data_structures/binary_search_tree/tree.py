# pypi
from attrs import define

# this project
from .node import Node


class Tree:
    """Binary Search Tree

    Args:
     root: the root node for the tree
    """
    def __init__(self, root: Node=None) -> None:
        self.root = root
        return

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
