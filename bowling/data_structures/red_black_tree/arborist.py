# this project
from bowling.data_structures.red_black_tree import tree as rb_tree


class Arborist:
    """An arborist to take care of trees

    Args:
     tree: tree to take care of
    """
    def __init__(self, tree: rb_tree.RedBlackTree):
        self.tree = tree
        return

    def left_rotate(self, node: rb_tree.Node) -> None:
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

    def right_rotate(self, node: rb_tree.Node) -> None:
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

    def insert(self, node: rb_tree.Node) -> None:
        """Insert the node into to the tree
    
        Args:
         node: node to insert into the tree
        """
        hunter = rb_tree.ROOT_PARENT
        hound = self.tree.root
    
        while hound is not rb_tree.LEAF:
            hunter = hound
            if node > hound:
                hound = hound.right
            else:
                hound = hound.left
        
        node.parent = hunter
    
        if hunter is rb_tree.ROOT_PARENT:
            self.tree.root = node
        node.left = rb_tree.LEAF
        node.right = rb_tree.LEAF
        node.color = rb_tree.Color.RED
        self.insert_fixup(node)
        return

    def insert_fixup(self, node: rb_tree.Node) -> None:
        """Fix-up the red-black properties after an insert
    
        Args:
         node: the node that was just inserted
        """
        while node.parent.is_red:
            if node.parent.is_left:
                uncle = node.parent.parent.right
                self.fixup_side(node, uncle,
                                swap_and_rotate=node.is_right,
                                left=True)
            else:
                uncle = node.parent.parent.left
                self.fixup_side(node, uncle,
                                swap_and_rotate=node.is_left,
                                left=False)
        self.tree.root.color = rb_tree.Color.BLACK
        return

    def fixup_side(self, node: rb_tree.Node, uncle: rb_tree.Node,
                   swap_and_rotate: bool=True, left: bool=True) -> None:
        """Fixup either the left or the right sides
    
        Args:
         node: the node that we're fixing
         uncle: the node's parent's sibling
         swap_and_rotate: whether we need to do a swap and rotation
         left: if the node's parent is a left child
        """
        first_rotate = self.left_rotate if left else self.right_rotate
        final_rotate = self.right_rotate if left else self.left_rotate
        
        if uncle.is_red:
            node.parent.color = rb_tree.Color.BLACK
            node.parent.parent.color = rb_tree.Color.RED
            uncle.color = rb_tree.Color.BLACK
            node = node.parent.parent
        else:
            if swap_and_rotate:
                node = node.parent
                first_rotate(node)
            node.parent.color = rb_tree.Color.BLACK
            node.parent.parent.color = rb_tree.Color.RED
            
            final_rotate(node.parent.parent)
        return
