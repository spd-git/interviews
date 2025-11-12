def bubble_sort(arr: [int]):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                swapped = True

        if not swapped:
            break


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    print(test_arr)
    bubble_sort(test_arr)
    print(test_arr)
    test_arr.sort(reverse=True)
    print(test_arr)
    bubble_sort(test_arr)
    print(test_arr)

