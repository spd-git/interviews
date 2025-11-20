

class BinarySearch:

    def __init__(self, arr):
        self.arr = arr

    def search(self, key):
        left = 0
        right = len(self.arr) - 1
        while right >= left:
            mid = left + (right - left) // 2
            mid_val = self.arr[mid]
            if mid_val == key:
                return mid
            elif mid_val < key:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":
    test_arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    obj = BinarySearch(test_arr)
    print(obj.search(5))
    for i in test_arr:
        print(obj.search(i))
