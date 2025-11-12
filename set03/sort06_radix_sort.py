def radix_sort(arr: [int]):
    n = len(arr)
    if n <= 1:
        return

    max_val = max(arr)
    radix_arr = [[] for _ in range(10)]
    exp = 1

    while max_val // exp > 0:
        while len(arr) > 0:
            val = arr.pop()
            rad_idx = (val // exp) % 10
            radix_arr[rad_idx].append(val)

        for bucket in radix_arr:
            while len(bucket) > 0:
                arr.append(bucket.pop())

        exp *= 10


def _radix_sort(arr: [int]):
    n = len(arr)
    if n <= 1:
        return
    radix_arr = [[] for _ in range(10)]
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        while len(arr) > 0:
            val = arr.pop()
            radix_idx = (val // exp) % 10
            radix_arr[radix_idx].append(val)

        for bucket in radix_arr:
            while len(bucket) > 0:
                val = bucket.pop()
                arr.append(val)

        exp *= 10


if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    radix_sort(test_arr)
    print(test_arr)

    test_arr.sort(reverse=True)
    print(test_arr)
    radix_sort(test_arr)
    print(test_arr)

