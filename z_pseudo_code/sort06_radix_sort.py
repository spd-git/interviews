
def radix_sort(arr):
    n = len(arr)
    if n <= 1:
        return

    exp = 1
    max_val = max(arr)
    rad_arr = [[] for _ in range(10)]

    while max_val // exp > 0:
        while len(arr) > 0:
            val = arr.pop()
            rad_idx = ( val // exp) % 10
            rad_arr[rad_idx].append(val)

        for bucket in rad_arr:
            while len(bucket) > 0:
                arr.append(bucket.pop())

        exp *= 10


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    radix_sort(test_arr)
    print(test_arr)

    test_arr.sort(reverse=True)
    print(test_arr)
    radix_sort(test_arr)
    print(test_arr)

    for i, j in zip(test_arr, [1, 1, 2, 3, 6, 8, 10]):
        if i != j:
            print("DINT WORK")
