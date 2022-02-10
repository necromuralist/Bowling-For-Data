# pypi
# https://www.attrs.org/en/stable/index.html
from attrs import define


@define
class MaxHeap:
    """Build and maintain a max-heap

    If you pass in the heap as a list pre-pend it with Infinity

    Otherwise use ~heap = MaxHeap.from_list(elements)~ to build it
    """
    INFINITY = float("inf")
    NEGATIVE_INFINITY = -INFINITY
    ROOT_NODE = 1

    heap: list = [INFINITY]
    _size: int = None

    @classmethod
    def from_list(cls, heap: list):
        """Builds a max-heap instance from the starter list
    
        Args:
         heap: list of elements to dump on the heap
        
        Returns:
         MaxHeap instance with the heap list added
        """
        return cls(heap = [cls.INFINITY] + heap)

    @property
    def size(self) -> int:
        """The size of the max heap"""
        if self._size is None:
            self._size = len(self.heap) - 1
        return self._size
    
    @size.setter
    def size(self, new_size) -> int:
        """Set the size of the max heap
        
        Args:
         new_size: how much of the list is in the heap
    
        Raises:
         AssertionError if the size is out of bounds for the list
        """
        assert 0 <= new_size <= self.length
        self._size = new_size
        return

    @property
    def length(self) -> int:
        """The size of the array for the heap
    
        Warning:
         This includes the padding at the beginning of the list
        """
        return len(self.heap)

    @property
    def maximum(self):
        """The value in the root node"""
        return self.heap[self.ROOT_NODE]

    def parent(self, node: int) -> int:
        """Find the parent of a node
        
        Args:
         node: the index of the node to check
    
        Returns:
         the index of the parent of the node
        """
        return node//2

    def left_child(self, parent: int) -> int:
        """Find the left child of a parent
    
        Args:
         parent: the index of the parent node
    
        Returns:
         index of the left child of the parent
        """
        return 2 * parent

    def right_child(self, parent: int) -> int:
        """Find the right child of a parent
    
        Args:
         parent: the index of the parent node
    
        Returns:
         index of the right child of the parent
        """
        return 2 * parent + 1

    def heapify_subtree(self, node: int):
        """Heapify the tree rooted at the node
        
        Args:
         node: index of the node to compare to its descendants
        """
        left, right = self.left_child(node), self.right_child(node)
        largest = node
        
        if left <= self.size and self.heap[left] > self.heap[largest]:
            # the left child was larger than the current parent node
            largest = left
    
        if right <= self.size and self.heap[right] > self.heap[largest]:
            # the right child is larger than the left and the current parent
            largest = right
    
        if largest != node:
            # the current parent is out of place, swap it
            self.heap[node], self.heap[largest] = (self.heap[largest],
                                                   self.heap[node])
    
            # after the swap the item at "largest" is the "node" we started with
            # so try it again
            self.heapify_subtree(largest)
        return

    def increase_key(self, node, key):
        """Increase the node's value
    
        Args:
         node: index of node in heap to change
         key: new value for the node
    
        Raises:
         AssertionError if new value isn't larger than the previous value
        """
        assert key > self.heap[node], (f"{key} not greater than previous value {self.heap.node}")
        self.heap[node] = key
    
        while (node > self.ROOT_NODE and
               self.heap[self.parent(node)] < self.heap[node]):
            self.heap[node], self.heap[self.parent(node)] = (
                self.heap[self.parent(node)], self.heap[node])
            node = self.parent(node)
        return

    def insert(self, key):
        """Insert the key into the heap
    
        Args:
         key: orderable item to insert into the heap
        """
        self.size += 1
        self.heap[self.size - 1] = self.NEGATIVE_INFINITY
        self.increase_key(self.size - 1, key)
        return

    def __call__(self):
        """Heapifies the heap
    
        Raises:
         AssertionError: something bad happened and the Heap Property failed
        """
        for parent in reversed(range(1, self.size//2 + 1)):
            self.heapify_subtree(parent)
    
        self.check_rep()
        return

    def check_rep(self) -> None:
        """Checks the heap property
    
        Raises:
         AssertionError: the heap property has been violated
        """
        for node in range(1, self.size):
            assert self.heap[self.parent(node)] >= self.heap[node], (
                f"Parent node {self.parent(node)} = {self.heap[self.parent(node)]} "
                f"not >= {node}={self.heap[node]}")
        return

    def __getitem__(self, node: int):
        """Gets an item from the heap
            
        Args: 
         node: index of the heap to get the value
        """
        return self.heap[node]
    
    def __setitem__(self, node, value):
        """Sets the value at the node in the heap
    
        Args:
         node: index of the heap to set the value
         value: what to set the location in the heap to
        """
        self.heap[node] = value
        return
