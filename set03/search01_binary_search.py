
def binary_search(arr: [int], val: int):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    test_arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    print(binary_search(test_arr, 3))
    print(binary_search(test_arr, 13))
    print(binary_search(test_arr, 2))
    for i in test_arr:
        print(binary_search(test_arr, i))
