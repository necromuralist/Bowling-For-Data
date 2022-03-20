# python
from __future__ import annotations
from collections import namedtuple
from enum import IntEnum

# this project
from bowling.types import Orderable


class Color(IntEnum):
    """red or black"""
    RED = 1
    BLACK = 2


NIL_KEY = "NIL"
NIL = namedtuple("NIL", ["key", "color"],
                 defaults=[NIL_KEY, Color.BLACK])()


class Node:
    """A Node in a Binary Search Tree

    Args:
     key: item to compare nodes
     color: RED or BLACK
     parent: parent of this node
     left: left child
     right: right child
    """
    def __init__(self, key: Orderable, color: Color,
                 parent: Node=NIL,
                 left: Node=NIL, right: Node=NIL) -> None:
        self.key = key
        self.color = color
        self._parent = None
        self.parent = parent
        self._left = None
        self.left = left
        self._right = None
        self.right = right
        return

    @property
    def parent(self) -> Node:
        """The parent of this node"""
        return self._parent
    
    @parent.setter
    def parent(self, parent_: Node) -> None:
        """Sets the parent and updates the parent
    
        Warning:
         this will clobber the parent's child if there's a node where this should
        be
    
        Args:
         parent: to add to self
    
        Raises:
         AssertionError if parent and self have same key
        """
        if parent_.key == NIL_KEY:
            self._parent = parent_
            return
    
        if self == parent_:
            raise AssertionError(f"Self ({self}) cannot equal parent ({parent_})")
        
        # since the left and right assignments update the parent
        # we need a hack to get around the setters or you end up
        # with an infinite loop - we set left, they set parent, we set left,...
        if self < parent_:
            parent_._left = self
        else:
            parent_._right = self
    
        self._parent = parent_        
        return

    @property
    def left(self) -> Node:
        """The left child"""
        return self._left
    
    @left.setter
    def left(self, new_left: Node) -> None:
        """Sets the left and its parent
    
        Raises:
         AssertionError if left isn't less than self
    
        Args:
         new_left: a node to be the left child or None
        """
        if new_left.key == NIL_KEY:
            self._left = new_left
            return
            
        assert new_left < self, f"Left ({new_left} not < self {self})"
        new_left.parent = self
        self._left = new_left
        return

    @property
    def right(self) -> Node:
        """The right child"""
        return self._right
    
    @right.setter
    def right(self, new_right: Node) -> None:
        """Sets the right and its parent
    
        Raises:
         AssertionError if right isn't greater than self
    
        Args:
         new_right: a node to be the right child or None
        """
        if new_right is NIL:
            self._right = new_right
            return
            
        assert new_right > self, f"right ({new_right} not > self ({self})"
        new_right.parent = self
        self._right = new_right
        return

    def __eq__(self, other: Node) -> bool:
        """Check if the other node has an equal key
            
        """
        return hasattr(other, "key") and self.key == other.key

    def __lt__(self, other: Node) -> bool:
        """See if this key is less than the other's
         
        Raises:
         AttributeError: the other thing doesn't have a key
    
        Returns:
         self < other
        """
        if not hasattr(other, "key"):
            raise AttributeError(f"'<' not supported between '{type(self)}' "
                            "and '{type(other)}'")
        return self.key < other.key

    def __le__(self, other: Node) -> bool:
        """See if this key is less than or equal to other's
    
        Raises:
         AttributeError: other doesn't have key
    
        Returns:
         self <= other
        """
        if not hasattr(other, "key"):
            raise AttributeError(f"'<' not supported between '{type(self)}' "
                            "and '{type(other)}'")
        return self.key <= other.key

    def check_node(self) -> None:
        """Checks that the Binary Search Tree Property holds
    
        Raises:
         AssertionError: Binary Search Tree Property violated or duplicates exist
        """
        # red-black property 1: every node is either red or black
        assert self.color in (Color.RED, Color.BLACK), f"Invalid Color: {self.color}"
    
        # red-black property 4: if a node is red, both children are black
        if self.color == Color.RED:
            assert Color.RED not in (self.left.color, self.right.color)
    
        if self.left is not NIL:
            assert self.left < self, f"Left: {self.left} not < Self: {self}"
            self.left.check_node()
    
        if self.right is not NIL:
            assert self.right > self, f"Right: {self.right} not > Self: {self}"
            self.right.check_node()
        return

    def __str__(self) -> str:
        """The key as a string"""
        return str(self.key)
