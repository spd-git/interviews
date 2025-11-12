
def heap_sort(arr: [int]):
    pass


def heapify(arr, n, i):
    pass


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


