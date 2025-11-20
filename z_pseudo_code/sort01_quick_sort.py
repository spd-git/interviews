
def quick_sort_recursive(arr: [int]):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort_recursive(left) + [pivot] + quick_sort_recursive(right)


if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort_recursive(test_arr)
    print(sorted_arr)
    for i, j in zip(sorted_arr, [1, 1, 2, 3, 6, 8, 10]):
        if i != j:
            print("DINT WORK")
