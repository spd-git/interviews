
def ternary_search(arr: [int], val: int):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == val:
            return mid1
        elif arr[mid2] == val:
            return mid2

        if arr[mid2] < val:
            low = mid2 + 1
        elif arr[mid1] > val:
            high = mid1 - 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1


if __name__ == "__main__":
    test_arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    print(ternary_search(test_arr, 3))
    print(ternary_search(test_arr, 13))
    print(ternary_search(test_arr, 2))
    print("------------------------------------")
    for i in test_arr:
        print(ternary_search(test_arr, i))
    print("------------------------------------")

