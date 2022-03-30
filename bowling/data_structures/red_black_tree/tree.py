# python
from __future__ import annotations
from collections import namedtuple
from enum import Enum

# this project
from bowling.types import Orderable


class Color(Enum):
    """red or black"""
    RED = 1
    BLACK = 2

NIL_KEY = "NIL"
NIL = namedtuple(
    "NIL", "key color parent left right is_red is_black",
    defaults=[NIL_KEY, Color.BLACK, None, None, None, False, True])()
LEAF = NIL
ROOT_PARENT = NIL


class Node:
    """A Node in a Binary Search Tree

    Args:
     key: item to compare nodes
     color: RED or BLACK
     parent: parent of this node
     left: left child
     right: right child
    """
    def __init__(self, key: Orderable, color: Color=None,
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
        if self._parent is None:
            self._parent = NIL
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
        if parent_ is NIL:
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
        if self._left is None:
            self._left = NIL
        return self._left
    
    @left.setter
    def left(self, new_left: Node) -> None:
        """Sets the left and its parent
    
        Raises:
         AssertionError if left isn't less than self
    
        Args:
         new_left: a node to be the left child or None
        """
        if new_left is NIL:
            self._left = new_left
            return
            
        assert new_left < self, f"Left ({new_left} not < self {self})"
        new_left.parent = self
        self._left = new_left
        return

    @property
    def right(self) -> Node:
        """The right child"""
        if self._right is None:
            self._right = NIL
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
                                 f"and '({other}): {type(other)}'")
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

    @property
    def is_left(self) -> bool:
        """True if this node is a left child"""
        return self is self.parent.left

    @property
    def is_right(self) -> bool:
        """True if this node is a right child"""
        return self.parent.right is self

    @property
    def is_red(self) -> bool:
        """True if the node is colored red"""
        return self.color is Color.RED

    @property
    def is_black(self) -> bool:
        """True if the node is colored black"""
        return self.color is Color.BLACK

    @property
    def is_root(self) -> bool:
        """True if the node is the root"""
        return self.parent is NIL

    def check_state(self) -> None:
        """Checks that the Binary Search Tree Property holds
    
        Raises:
         AssertionError: Binary Search Tree Property violated or duplicates exist
        """
        # red-black property 1: every node is either red or black
        assert self.color in (Color.RED, Color.BLACK), f"Invalid Color: {self.color}"
    
        # red-black property 4: if a node is red, both children are black
        if self.color is Color.RED:
            assert (self.left.color is Color.BLACK and
                    self.right.color is Color.BLACK),\
                (f"Parent: {self.color} Left: {self.left.color} "
                 f"Right: {self.right.color}. "
                 "Both Children of a Red parent must be Black")
    
        if self.left is not NIL:
            assert self.left < self, f"Left: {self.left} not < Self: {self}"
            self.left.check_state()
    
        if self.right is not NIL:
            assert self.right > self, f"Right: {self.right} not > Self: {self}"
            self.right.check_state()
        return

    def __str__(self) -> str:
        """The key as a string"""
        return str(self.key)


class RedBlackTree:
    """The Holder of the Red-Black Tree

    Args:
     root: the root node of the tree
    """
    def __init__(self, root: Node=NIL):
        self.root = root
        return
