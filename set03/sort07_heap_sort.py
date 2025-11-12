
def heap_sort(arr: [int]):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        swap(arr, i, 0)
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # chk left child exists and is larger than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # chk right child exists and is larger than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # change root, if needed
    if largest != i:
        swap(arr, i, largest)

        # heapify the root
        heapify(arr, n, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    heap_sort(test_arr)
    print(test_arr)

    test_arr.sort(reverse=True)
    print(test_arr)
    heap_sort(test_arr)
    print(test_arr)

