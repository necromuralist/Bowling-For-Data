from bowling.data_structures.red_black_tree import tree as rb_tree


class Forester:
    """The forester manages the tree

    Args:
     tree: tree to manage
     enforce_properties: check that the black-heights are the same
    """
    def __init__(self, tree: rb_tree.RedBlackTree=None,
                 enforce_properties: bool=False) -> None:
        self.tree = tree
        self.enforce_properties = enforce_properties
        return

    def search(self, key) -> rb_tree.Node:
        """Searches the tree for the node with the matching key
    
        Args:
         key: node's key to search for
    
        Returns:
         the node with the key or None if it isn't in the tree
        """
        node = self.tree.root
        while node is not rb_tree.LEAF and key != node.key:
            if key < node.key:
                node = node.left
            else:
               node = node.right
        return node

    def min(self, node: rb_tree.Node=None) -> rb_tree.Node:
        """Returns the node with the smallest key
    
        Args:
         node: a node to use as the starting root
        """
        if node is None:
            node = self.tree.root
    
        while node.left is not rb_tree.LEAF:
            node = node.left
        return node

    def max(self, root: rb_tree.Node=None) -> rb_tree.Node:
        """Returns the node with the largest key
    
        Args:
         root: subtree root to start at
    
        Returns:
         node with the largest key in tree/subtree
        """
        if root is None:
            root = self.tree.root
        while root.right is not rb_tree.LEAF:
            root = root.right
        return root

    @property
    def height(self) -> int:
        """The length of the longest path starting at the root
        
        Returns:
         number of edges from root to furthest leaf
        """
        return self.tree_height(self.tree.root)

    @property
    def black_height(self) -> int:
        """The number of black nodes below the root
        """
        return self.find_black_height(self.tree.root)

    def tree_height(self, node: rb_tree.Node=None) -> int:
        """The length of the longest path starting at the node
    
        Args:
         the node to start the measurement from
    
        Returns:
         number of edges from root to furthest leaf
        """
        if node is rb_tree.LEAF:
            return -1
    
        left = self.tree_height(node.left) + 1
        right = self.tree_height(node.right) + 1
        return max(left, right)

    def find_black_height(self, node: rb_tree.Node=None) -> int:
        """Find the number of black nodes below a node
    
        Note:
         This assumes that the starting node is black. In the cases where it's red
         it will be one more than the true height
    
        Args:
         node: base node to use
        """
        if node is rb_tree.LEAF:
            return 0
    
        add_for_color = 1 if node.is_black else 0
        left = self.find_black_height(node.left) + add_for_color
        right = self.find_black_height(node.right) + add_for_color
        if self.enforce_properties:
            assert left == right, f"Black Height: Left={left} Right={right}"
        return max((left, right))
