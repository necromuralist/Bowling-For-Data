# pypi
# https://www.attrs.org/en/stable/index.html
from attrs import define

# this project
from bowling.data_structures.heap import MaxHeap

@define
class HeapSort:
    """Sort using a heap

    Args:
     items: collection of items for the sort
    """
    items: list
    _heap: MaxHeap=None

    @property
    def heap(self) -> MaxHeap:
        """The heap of items"""
        if self._heap is None:
            self._heap = MaxHeap.from_list(self.items)
            self._heap()
        return self._heap

    @property
    def without_root(self) -> list:
        """The items without the root """
        return self.heap.heap[self.heap.ROOT_NODE:]

    def __call__(self):
        """sorts the items"""
        self.heap()
        for node in range(self.heap.size, 1, -1):
            self.heap.heap[self.heap.ROOT_NODE], self.heap.heap[node] = (
                self.heap.heap[node],
                self.heap.maximum)
            self.heap.size -= 1
            self.heap()
        return
