# python
from __future__ import annotations

# this project
from bowling.types import Orderable





class Node:
    """A Node in a Binary Search Tree

    Args:
     key: item to compare nodes
     parent: parent of this node
     left: left child
     right: right child
    """
    def __init__(self, key: Orderable, parent: Node=None,
                 left: Node=None, right: Node=None) -> None:
        self.key = key
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
        if parent_ is None:
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
        if new_left is None:
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
        if new_right is None:
            self._right = new_right
            return
            
        assert new_right > self, f"right ({new_right} not > self ({self})"
        new_right.parent = self
        self._right = new_right
        return

    def __eq__(self, other: Node) -> bool:
        """Check if the other node has an equal key
            
        """
        return type(self) == type(other) and self.key == other.key

    def __lt__(self, other: Node) -> bool:
        """See if this key is less than the other's
    
        Raises:
         TypeError: the other thing doesn't have a key
        """
        if not type(self) == type(other):
            raise TypeError(f"'<' not supported between '{type(self)}' "
                            "and '{type(other)}'")
        return self.key < other.key

    def __le__(self, other: Node) -> bool:
        """See if this key is less than or equal to other's"""
        if not type(self) == type(other):
            raise TypeError(f"'<' not supported between '{type(self)}' "
                            "and '{type(other)}'")
        return self.key <= other.key
    

    def check_node(self) -> None:
        """Checks that the Binary Search Tree Property holds
    
        Raises:
         AssertionError: Binary Search Tree Property violated or duplicates exist
        """
        assert self.parent is None or type(self.parent) is Node,\
            f"self.parent={self.parent}, type={type(self.parent)}"
        if self.left is not None:
            assert self.left < self, f"Left: {self.left} not < Self: {self}"
            self.left.check_node()
    
        if self.right is not None:
            assert self.right > self, f"Right: {self.right} not > Self: {self}"
            self.right.check_node()
        return

    def __str__(self) -> str:
        """The key as a string"""
        return str(self.key)
