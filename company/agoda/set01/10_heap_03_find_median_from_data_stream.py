"""Find Median from Data Stream problem implementation."""
import heapq


class MedianFinder:
    """Maintain two heaps to support addNum and findMedian operations."""

    def __init__(self) -> None:
        self.lower: list[int] = []  # max-heap via negative values
        self.higher: list[int] = []  # min-heap

    def add_num(self, num: int) -> None:
        if not self.lower or num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.higher, num)

        # Balance the heaps so that their sizes differ at most by one
        if len(self.lower) > len(self.higher) + 1:
            heapq.heappush(self.higher, -heapq.heappop(self.lower))
        elif len(self.higher) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.higher))

    def find_median(self) -> float:
        if len(self.lower) > len(self.higher):
            return float(-self.lower[0])
        return (-self.lower[0] + self.higher[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    for number in [1, 2, 3]:
        mf.add_num(number)
    assert mf.find_median() == 2
