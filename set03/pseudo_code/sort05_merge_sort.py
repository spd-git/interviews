
def merge_sort(arr):
    pass


def merge(left, right):
    pass


if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    print(test_arr)
    sorted_arr = merge_sort(test_arr)
    print(sorted_arr)

    test_arr.sort(reverse=True)
    print(test_arr)
    print(merge_sort(test_arr))

    for i, j in zip(sorted_arr, [1, 1, 2, 3, 6, 8, 10]):
        if i != j:
            print("DINT WORK")
