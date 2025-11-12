def quick_sort_recursive(arr: [int]):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort_recursive(less_than_pivot) + [pivot] + quick_sort_recursive(greater_than_pivot)


def quick_sort(arr: [int]):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]


if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort_recursive(test_arr)
    print(sorted_arr)
