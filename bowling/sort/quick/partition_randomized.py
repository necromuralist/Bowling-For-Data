# python
# For python 3.9 and newer you want to import from collections.abc
# But Ubuntu 21.10 has pypy 3.7 which needs the version from typing
# for what we want here
from typing import Callable, MutableSequence, TypeVar

import random

Orderable = TypeVar("Orderable")
Partition = Callable[[MutableSequence[Orderable], int, int], int]


def partition_randomized(collection: MutableSequence[Orderable],
                         left: int, right: int,
                         pivot: int,
                         partition: Partition) -> int:
    """Partitions the collection around a random element in the list

    Args:
     collection: the list to partition
     left: index of the first element in the sub-list to partition
     right: index of the last element in the sub-list to partition
     pivot: location of the pivot element
     partition: the partition function to use

    Returns:
     the index of the pivot element
    """
    random_index = random.randrange(left, right + 1)
    collection[pivot], collection[random_index] = (collection[random_index],
                                                   collection[pivot])
    return partition(collection, left, right)
