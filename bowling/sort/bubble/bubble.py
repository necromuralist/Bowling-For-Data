# python
from typing import List


class BubbleCounter:
    """Keeps track of counts during the bubble-sort

    Args:
     elements: of (in-place) sortable elements
    """
    elements: List[int]
    comparisons: int
    swaps: int

    def __init__(self, elements: list):
        self.elements = elements
        self.comparisons = 0
        self.swaps = 0
        return

    

    def __call__(self) -> None:
        """Sorts the list in place
    
        Postcondition:
         - elements list is in sorted order
        """
        all_but_one = len(self.elements) - 1
        for items_bubbled_up in range(all_but_one):
            for left_hand in range(all_but_one - items_bubbled_up):
                self.comparisons += 1
                right_hand = left_hand + 1
                if self.elements[right_hand] < self.elements[left_hand]:
                    (self.elements[left_hand],
                     self.elements[right_hand]) = (self.elements[right_hand],
                                                   self.elements[left_hand])
                    self.swaps += 1
        return

class BubbleTracker:
    """Keeps track of locations of elements during the sort

    Args:
     elements: list of sortable items
    """
    def __init__(self, elements: list):
        self.elements = elements
        self._swaps = None
        return

    @property
    def swaps(self) -> dict:
        """The location of each element when a swap is made"""
        if self._swaps is None:
            self._swaps = {
                element: [index] for index, element in enumerate(self.elements)}
        return self._swaps

    def __call__(self):
        """Does the bubble-sort and tracks the locations"""
        all_but_one = len(self.elements) - 1
        # hack to initialize the swaps
        self.swaps
        for items_bubbled_up in range(all_but_one):
            for left_hand in range(all_but_one - items_bubbled_up):
                right_hand = left_hand + 1            
                if self.elements[right_hand] < self.elements[left_hand]:
                    (self.elements[left_hand],
                     self.elements[right_hand]) = (self.elements[right_hand],
                                                   self.elements[left_hand])
                    for index, element in enumerate(self.elements):
                        self.swaps[element].append(index)
        return
