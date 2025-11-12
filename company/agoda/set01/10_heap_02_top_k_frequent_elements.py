"""Top K Frequent Elements problem implementation."""
import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Return k most frequent elements using a heap."""
    counts = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, counts.items(), key=lambda pair: pair[1])]


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
