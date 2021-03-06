# python
from __future__ import annotations
from typing import TYPE_CHECKING

# this project
if TYPE_CHECKING:
    from .node import Node
    from .tree import Tree


class Query:
    """Holds a tree and performs queries on it

    Args:
     tree: A Binary Search Tree
    """
    def __init__(self, tree: Tree):
        self.tree = tree
        return

    def search(self, key) -> Node:
        """Searches the tree for the node with the matching key
    
        Args:
         key: node's key to search for
    
        Returns:
         the node with the key or None if it isn't in the tree
        """
        node = self.tree.root
        while node is not None and key != node.key:
            if key < node.key:
                node = node.left
            else:
               node = node.right
        return node

    def min(self, node: Node=None) -> Node:
        """Returns the node with the smallest key
    
        Args:
         node: a node to use as the starting root
        """
        if node is None:
            node = self.tree.root
    
        while node.left is not None:
            node = node.left
        return node

    def max(self, root: Node=None) -> Node:
        """Returns the node with the largest key
    
        Args:
         root: subtree root to start at
    
        Returns:
         node with the largest key in tree/subtree
        """
        if root is None:
            root = self.tree.root
        while root.right is not None:
            root = root.right
        return root

    def successor(self, node: Node) -> Node:
        """Returns the next largest node
    
        Args:
         node: the node who's successor to find
    
        Returns:
         successor node to the input node
        """
        if node.right is not None:
            return self.min(node.right)
    
        successor = node.parent
        while successor is not None and node == successor.right:
            node = successor
            successor = successor.parent
        return successor

    def predecessor(self, node: Node) -> Node:
        """Returns the predecessor node
    
        Args:
         node: the node whose predecessor we want
    
        Returns:
         largest node smaller than given node
        """
        if node.left is not None:
            return self.max(node.left)
        predecessor = node.parent
        while predecessor is not None and node == predecessor.left:
            node, predecessor = predecessor, predecessor.parent
        return predecessor

    @property
    def height(self) -> int:
        """The length of the longest path starting at the root
        
        Returns:
         number of edges from root to furthest leaf
        """
        return self.tree_height(self.tree.root)

    def tree_height(self, node: Node=None) -> int:
        """The length of the longest path starting at the node
    
        Args:
         the node to start the measurement from
    
        Returns:
         number of edges from root to furthest leaf
        """
        if node is None:
            return -1
    
        left = self.tree_height(node.left) + 1
        right = self.tree_height(node.right) + 1
        return max(left, right)
