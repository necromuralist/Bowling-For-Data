# pypi
from attrs import define

# this project
from bowling.data_structures.red_black_tree import tree as rb_tree


@define
class Rotator:
    """A rotator of nodes and their children

    Args:
     tree: the tree that the parent belongs to
    """
    tree: rb_tree.RedBlackTree

    def left(self, node: rb_tree.Node) -> None:
        """Rotates the node with its right child
    
        Args:
         node: the parent node to rotate
        """
        new_parent = node.right
        node.right= new_parent.left
    
        new_parent.parent = node.parent
    
        if node.is_root:
            self.tree.root = new_parent
        new_parent.left = node
        return

    def right(self, node: rb_tree.Node) -> None:
        """Rotates the node with its left child
    
        Args:
         node: the parent node to rotate
        """
        previous_child = node.left
        node.left = previous_child.right
        previous_child.parent = node.parent
    
        if node.is_root:
            self.tree.root = previous_child
        previous_child.right = node
        return
