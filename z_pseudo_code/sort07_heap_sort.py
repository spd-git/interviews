
def heap_sort(arr: [int]):
    n = len(arr)
    if n <= 1:
        return

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        swap(arr, i, 0)
        heapify(arr, n, 0)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if i != largest:
        swap(arr, i, largest)
        heapify(arr, n, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    test_arr = [x for x in range(30)]
    heap_sort(test_arr)

    test_arr = [3, 6, 8, 10, 1, 2, 1]
    heap_sort(test_arr)
    print(test_arr)

    test_arr.sort(reverse=True)
    print(test_arr)
    heap_sort(test_arr)
    print(test_arr)

    for i, j in zip(test_arr, [1, 1, 2, 3, 6, 8, 10]):
        if i != j:
            print("DINT WORK")


