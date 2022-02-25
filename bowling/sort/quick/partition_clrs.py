# python
from collections.abc import MutableSequence


def partition_clrs(collection: MutableSequence, left: int, right: int) -> int:
    """Partitions the collection around the last element

    Args:
     collection: the list to partition
     left: index of the first element in the sub-list to partition
     right: index of the last element in the sub-list to partition

    Returns:
     the index of the pivot element
    """
    pivot_element = collection[right]
    lower_bound = left - 1
    for upper_bound in range(left, right):
        if collection[upper_bound] <= pivot_element:
            lower_bound += 1
            (collection[lower_bound],
             collection[upper_bound]) = (collection[upper_bound],
                                         collection[lower_bound])
    pivot = lower_bound + 1
    (collection[pivot],
     collection[right]) = (collection[right],
                           collection[pivot])
    return pivot
