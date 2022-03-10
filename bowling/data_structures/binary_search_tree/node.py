# python
from __future__ import annotations

# from pypi
# https://www.attrs.org/en/stable/index.html
from attrs import define

# this project
from bowling.types import Orderable

@define
class Node:
    """A Node in a Binary Search Tree

    Args:
     key: item to compare nodes
     parent: parent of this node
     left: left child
     right: right child
    """
    key: Orderable
    parent: Node=None
    left: Node=None
    right: Node=None

    def __eq__(self, other: Node) -> bool:
        """Check if the other node has an equal key"""
        return self.key == other.key

    def __lt__(self, other: Node) -> bool:
        """See if this key is less than the other's"""
        return self.key < other.key

    def __le__(self, other: Node) -> bool:
        """See if this key is less than or other's"""
        return self.key <= other.key
    

    def check_node(self) -> None:
        """Checks that the Binary Search Tree Property holds
    
        Raises:
         AssertionError: Binary Search Tree Property was violated
        """
        assert self.parent is None or type(self.parent) is Node
        if self.left is not None:
            assert self.left <= self
            self.left.check_node()
    
        if self.right is not None:
            assert self.right >= self
            self.right.check_node()
        return

    def __str__(self) -> str:
        """The key as a string"""
        return str(self.key)
