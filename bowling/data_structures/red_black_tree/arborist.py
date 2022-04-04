# this project
from bowling.data_structures.red_black_tree import tree as rb_tree
from bowling.data_structures.red_black_tree.rotator import Rotator

from bowling.data_structures.red_black_tree.forester import Forester


class Inserter:
    """Insert a node into the tree

    Args:
      tree: Red-Black-Tree to insert nodes into
    """
    def __init__(self, tree: rb_tree.RedBlackTree) -> None:
        self._tree = None
        self.tree = tree
        self._rotate: Rotator = None
        return

    @property
    def tree(self) -> rb_tree.RedBlackTree:
        """The tree we're inserting nodes into"""
        return self._tree

    @tree.setter
    def tree(self, sapling: rb_tree.RedBlackTree) -> None:
        """stores the tree, resets other objects that used the prior tree"""
        self._tree = sapling
        self._rotate = None
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
        self.fixup(node)
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
        first_rotate = self.rotate.left if left else self.rotate.right
        final_rotate = self.rotate.right if left else self.rotate.left
        
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

    def fixup(self, node: rb_tree.Node) -> None:
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

    def __call__(self, node: rb_tree.Node) -> None:
        """Inserts the node into the tree
    
        this is an alias for the ``insert`` method
    
        Args:
         node: the node to insert 
        """
        return self.insert(node)


class Deleter:
    """Deletes nodes

    Args:
     tree: the RedBlackTree to update
    """
    def __init__(self, tree: rb_tree.RedBlackTree) -> None:
        self._tree = None
        self.tree = tree
        self._forester = None
        self._rotate = None
        return

    @property
    def tree(self) -> rb_tree.RedBlackTree:
        """The tree we're inserting nodes into"""
        return self._tree
    
    @tree.setter
    def tree(self, sapling: rb_tree.RedBlackTree) -> None:
        """stores the tree, resets other objects that used the prior tree"""
        self._tree = sapling
        self._rotate = None
        self._forester = None
        return

    

    @property
    def forester(self) -> Forester:
        """A forester to measure the tree"""
        if self._forester is None:
            self._forester = Forester(tree=self.tree)
        return self._forester

    def transplant(self, unwanted: rb_tree.Node,
                   replacement: rb_tree.Node) -> None:
        """Replace one node with another in the tree
    
        Gives replacement the parent of replaced, doesn't remove
        parent from replaced
    
        Args:
         unwanted: node to remove
         replacement: node to replace replaced
        """
        if unwanted.is_root:
            self.tree.root = replacement
        elif unwanted.is_left:
            unwanted.parent.left = replacement
        else:
            unwanted.parent.right = replacement
        replacement.parent = unwanted.parent
        return

    def delete(self, unwanted: rb_tree.Node) -> None:
        """Delete a node
    
        Args:
         unwanted: the node to delete
        """
        needs_fixing = unwanted.is_black
    
        if unwanted.left is rb_tree.LEAF:
            unwanted_child = unwanted.right
            self.transplant(unwanted, unwanted_child)
        elif unwanted.right is rb_tree.LEAF:
            unwanted_child = unwanted.left
            self.transplant(unwanted, unwanted_child)
        else:
            adopter = self.forester.min(unwanted.right)        
            needs_fixing = unwanted.is_black
            unwanted_child = adopter.right
            if adopter.parent is unwanted:
                unwanted_child.parent = adopter
            else:
                self.transplant(adopter, unwanted_child)
                adopter.right = unwanted.right
                adopter.right.parent = adopter
            self.transplant(unwanted, adopter)
            adopter.left = unwanted.left
            adopter.left.parent = adopter
            adopter.color = unwanted.color
        if needs_fixing:
            self.fixup(unwanted_child)
        return

    def fixup(self, node: rb_tree.Node)-> None:
        """Fixup the tree after a node deletion
    
        Args:
         node: the child of the deleted node
        """
        while not node.is_root and node.is_black:
            if node.is_left:
                self.fixup_one_side(node, left=True)
            else:
                self.fixup_one_side(node, left=False)
        node.color = rb_tree.Color.BLACK
        return

    def fixup_one_side(self, node: rb_tree.Node, left: bool=True) -> None:
        """Does either the case where the node is left or node is right"""
        child = node.parent.right if left else node.parent.left
        if child.is_red:
            child.color = rb_tree.Color.BLACK
            node.parent.color = rb_tree.Color.BLACK
            rotate = self.rotate.left if left else self.rotate.right
            rotate(node.parent)
            child = node.parent.right if left else node.parent.left
        if child.left.is_black and child.right.is_black:
            child.color = rb_tree.Color.RED
            node = node.parent
        else:
            if child.is_black:
                grandchild = child.left if left else child.right
                grandchild.color = rb_tree.Color.BLACK
                child.color = rb_tree.Color.RED
                rotate = self.rotate.right if left else self.rotate.left
                rotate(child)
                child = node.parent.right if left else node.parent.left
            child.color = node.parent.color
            node.parent.color = rb_tree.Color.BLACK
            grandchild = child.right if left else child.left
            grandchild.color = rb_tree.Color.BLACK
            rotate = self.rotate.left if left else self.rotate.right
            rotate(node.parent)
            node = self.tree.root
        return

    


class Arborist:
    """An arborist to take care of trees

    Args:
     tree: tree to take care of
    """
    def __init__(self, tree: rb_tree.RedBlackTree) -> None:
        self._tree = None
        self.tree = tree
        self._insert = None
        self._delete = None
        return

    @property
    def tree(self) -> rb_tree.RedBlackTree:
        """The tree we're inserting nodes into"""
        return self._tree

    @tree.setter
    def tree(self, sapling: rb_tree.RedBlackTree) -> None:
        """Sets the tree and wipes out other attributes that use it
    
        Args:
         sapling: new tree
        """
        self._tree = sapling
        self._insert = None
        self._delete = None
        return

    @property
    def insert(self) -> Inserter:
        """Something to insert nodes"""
        if self._insert is None:
            self._insert = Inserter(tree=self.tree)
        return self._insert

    @property
    def delete(self) -> Deleter:
        """A node deleter"""
        if self._delete is None:
            self._delete = Deleter(tree=self.tree)
        return self._delete
