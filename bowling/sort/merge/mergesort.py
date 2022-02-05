# python
from collections.abc import MutableSequence, Sequence

# this package
from .merge import merge, merge_clrs



def mergesort(collection: MutableSequence) -> int:
    """Sorts the collection using a recursive mergesort

    Args:
     collection: a mutable sequence

    Returns:
     runtime count
    """
    items = len(collection)
    count = 0
    if items > 1:
        middle = items//2
        left_stack = collection[:middle]
        right_stack = collection[middle:]
        assert len(left_stack) + len(right_stack) == items
        count += mergesort(left_stack)
        count += mergesort(right_stack)
        count += merge(left_stack, right_stack, collection)
    return count
