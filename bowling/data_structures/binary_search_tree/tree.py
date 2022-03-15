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
